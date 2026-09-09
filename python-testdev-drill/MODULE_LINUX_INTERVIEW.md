# Linux面试题

> 独立模块：Linux面试题
> 使用规则：与其他模块完全隔离，单独记录进度、错题、收藏、自建题。
> 来源：CSDN Linux 高频面试真题、运维排障面试题、测试环境排查实战题。

## 一、排查场景题（测试岗最高频）

### 1. 服务器磁盘满了怎么排查
- tags: 磁盘, 排查场景, 必考
- difficulty: medium
- frequency: 高频
- prompt: 服务器磁盘满了，你怎么排查？
- answer: 三步走：① df -h 看哪个挂载点满了；② du -sh /* 从大目录一层层往下钻，找到占空间最大的目录；③ find / -type f -size +500M 定位大文件。加分点：df -i 检查是不是 inode 用满（小文件太多）；用 truncate -s 0 清空被进程占用的日志而不是直接 rm（rm 后空间不释放）；建议 logrotate 日志轮转根治。

### 2. CPU 使用率很高怎么排查
- tags: CPU, 排查场景, 必考
- difficulty: medium
- frequency: 高频
- prompt: 服务很慢，怀疑 CPU 高，怎么排查？
- answer: ① top 看整体 CPU 和 load average（对比核数，超核数说明过载）；② ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head 找到占用最高的进程；③ top -Hp PID 下钻到线程级；④ 结合应用层分析（Java 用 jstack 看 GC/死循环）。加分点：区分 us（用户态）、sy（内核态）、wa（IO 等待）——wa 高说明瓶颈在磁盘不在计算。

### 3. 内存使用率高怎么排查
- tags: 内存, 排查场景, 必考
- difficulty: medium
- frequency: 高频
- prompt: 机器内存持续上涨，你怎么查？
- answer: ① free -h 看整体，重点看 available 而不是 free（free 小是正常的，buff/cache 可回收）；② ps aux --sort=-%mem | head 找高内存进程；③ vmstat 1 看 si/so 是否大于 0——大于 0 说明已触发 swap，内存真不足；④ dmesg | grep -i oom 查有没有 OOM Killer 记录。加分点：先区分是 page cache 正常占用还是进程泄漏，再决定优化方向。

### 4. 端口被占用了怎么处理
- tags: 网络, 排查场景
- difficulty: easy
- frequency: 高频
- prompt: 服务启动报 Address already in use，怎么处理？
- answer: ① ss -lntp | grep 8080 或 lsof -i :8080 查端口被哪个进程占用；② 拿到 PID 后 ps -p PID 确认是不是旧服务没退；③ 能优雅停止就 kill -15，不行再 kill -9；④ 重启服务并验证。记忆：查端口三件套 ss / lsof / netstat。

### 5. 服务器整体变慢，第一分钟看什么
- tags: 综合排查, 必考
- difficulty: medium
- frequency: 高频
- prompt: 用户反馈服务器慢，你第一分钟的排查顺序是什么？
- answer: 黄金 60 秒五连查：① uptime 看 load average 是否超核数；② free -h 看内存和 swap；③ df -h 看磁盘是否 100%；④ top 找最耗资源的进程；⑤ dmesg | tail 看有没有 OOM 或硬件错误。思路：先看资源总览，再定位到具体进程，最后进应用层分析。

### 6. df -h 显示有空间但写入报 No space left on device
- tags: 磁盘, inode, 加分
- difficulty: hard
- frequency: 加分题
- prompt: df -h 显示磁盘只用了 50%，但写入报 No space left on device，为什么？
- answer: 大概率是 inode 耗尽——大量小文件把 inode 用完了，跟磁盘空间是两码事。用 df -i 确认 inode 使用率；找小文件最多的目录清理后恢复。加分点：这是面试官爱挖的坑，能主动提 inode 就是加分。

## 二、高频命令题

### 7. top 命令能看到哪些信息
- tags: 监控, 必考
- difficulty: easy
- frequency: 高频
- prompt: top 命令能查看到哪些关键信息？
- answer: ① 系统概况：当前时间、运行时长、用户数；② load average 三个值（1/5/15 分钟负载，要对比 CPU 核数判断）；③ 任务情况：running/sleeping/zombie（僵尸进程数）；④ CPU 分布：us 用户态/sy 内核态/id 空闲/wa IO等待；⑤ 内存和 swap；⑥ 进程列表：PID、用户、CPU%、内存%、命令。加分点：按 P 按 CPU 排序、按 M 按内存排序。

### 8. top 和 htop 的区别
- tags: 监控
- difficulty: easy
- frequency: 中高频
- prompt: top 和 htop 有什么区别？
- answer: top 是系统自带的基础版；htop 是增强版：① 彩色界面信息密度高；② 支持鼠标和快捷键操作（F5 树形看进程父子关系、F4 过滤）；③ 可以直接在界面里 kill 进程、调优先级，不用记 PID；④ CPU/内存使用率可视化。生产环境一般装 htop 提效，但要理解 top 的指标含义才是根本。

### 9. kill -9 和 kill -15 的区别
- tags: 进程, 必考
- difficulty: medium
- frequency: 高频
- prompt: kill -9 和 kill -15 有什么区别？生产环境用哪个？
- answer: kill -15 发 SIGTERM，是"请进程退出"——进程可以清理资源（关文件、保存数据）后再退出，优雅终止；kill -9 发 SIGKILL，内核直接杀，进程没有任何机会清理，可能导致数据丢失或文件损坏。生产原则：**先 15 后 9**——先 kill -15 等待，超时无响应再 kill -9 兜底。systemctl stop 底层就是这个逻辑。

### 10. free 命令中 free 和 available 的区别
- tags: 内存, 常挖坑
- difficulty: medium
- frequency: 高频
- prompt: free -h 输出中 free 和 available 有什么区别？
- answer: free 是完全空闲的内存；available 是"真正还能给新进程用的内存" = free + buff/cache 中可回收的部分。Linux 会把空闲内存拿来做磁盘缓存，所以 free 很小是正常现象，不代表内存不足。判断内存是否紧张要看 available，以及 swap 的 si/so 是否大于 0。新手误区：看到 free 只有几百 M 就喊内存不足。

### 11. 怎么查看一个文件的最后 100 行
- tags: 文件, 基础
- difficulty: easy
- frequency: 高频
- prompt: 怎么查看文件的前 100 行和最后 100 行？
- answer: 前 100 行用 head -100 file；最后 100 行用 tail -100 file。延伸高频考点：tail -f file 实时滚动看日志；tail -F 与 -f 的区别——-f 基于文件描述符，日志轮转（改名）后就失效了，-F 基于文件名会自动追新文件，生产环境优先 -F。

### 12. find 和 grep 的区别
- tags: 搜索, 必考
- difficulty: easy
- frequency: 高频
- prompt: find 和 grep 的核心区别是什么？
- answer: find 按"文件属性"找文件（名字、大小、修改时间、类型），如 find /var/log -name "*.log" -mtime -3；grep 按"文本内容"找匹配（在文件里搜关键词），如 grep -C 3 "ERROR" app.log 显示前后 3 行。组合拳：find 找到文件后接 xargs grep 跨文件搜内容，如 find . -name "*.py" | xargs grep "password"。一句话：**find 找文件，grep 找内容**。

### 13. grep 统计关键字出现次数
- tags: 文本处理
- difficulty: easy
- frequency: 高频
- prompt: 怎么统计文件里某个关键字出现的次数？
- answer: grep -c "ERROR" app.log 统计包含关键字的行数；grep -o "ERROR" app.log | wc -l 统计关键字总出现次数（一行多次也计入）；grep -ci 忽略大小写。测试场景：统计日志错误数、接口 success 率都靠它。

### 14. sed 替换文件内容
- tags: 文本处理
- difficulty: medium
- frequency: 中高频
- prompt: 怎么替换文件中的某个值？
- answer: sed -i 's/旧值/新值/g' file——-i 直接改文件，s 表示替换，g 表示全局（一行内多次也替换）。延伸：sed -n '10,20p' file 打印 10-20 行；不加 -i 只预览不改文件。注意先不加 -i 验证效果再落盘。

### 15. awk 的常用用法
- tags: 文本处理
- difficulty: medium
- frequency: 中高频
- prompt: awk 常用在什么场景？举个例子。
- answer: awk 是按列处理文本的利器，适合"取某几列、按列统计"。常用：awk '{print $1}' 取第一列（如日志里取 IP）；awk -F: '{print $1}' /etc/passwd 指定冒号分隔；awk '$3 > 100 {print $1}' 条件过滤。测试场景：从接口日志取 URL 列统计、从 ls -l 输出取大小列求和。

### 16. chmod 755 是什么权限
- tags: 权限, 必考
- difficulty: easy
- frequency: 高频
- prompt: chmod 755 和 chmod u+x 分别是什么意思？
- answer: 权限数字 r=4、w=2、x=1，分三组：所有者/组/其他。755 = 所有者 rwx(7)、组 r-x(5)、其他 r-x(5)，常用于脚本和可执行文件。u+x 只给所有者加执行权限，不动其他人的权限。加分点：SUID（chmod u+s）让普通用户执行时临时获得所有者权限（passwd 就靠它），风险高，可用 find / -perm -4000 排查异常 SUID 文件。

### 17. 软链接和硬链接的区别
- tags: 文件系统
- difficulty: medium
- frequency: 中高频
- prompt: 软链接和硬链接有什么区别？
- answer: 软链接（ln -s）像快捷方式：存的是路径，源文件删除后链接失效，可跨分区、可指向目录。硬链接（ln）像同一个文件的另一个名字：指向同一个 inode，删源文件后硬链接仍可访问内容，但不能跨分区、不能给目录建。记忆：**软链接删源失效，硬链接删源还在**。

### 18. 怎么查看和结束进程
- tags: 进程
- difficulty: easy
- frequency: 高频
- prompt: 查看进程和结束进程的常用命令有哪些？
- answer: 查进程：ps aux | grep nginx（配合 grep 过滤）、ps -ef、pgrep -f nginx 直接拿 PID、pstree -p 看进程树。结束：kill PID（默认 -15）、kill -9 强杀、pkill nginx 按名字批量杀、killall nginx。注意 kill 前先确认 PID 对应的命令，别杀错。

### 19. 怎么查看僵尸进程
- tags: 进程, 加分
- difficulty: medium
- frequency: 加分题
- prompt: 什么是僵尸进程？怎么发现和处理？
- answer: 僵尸进程是子进程已退出但父进程没回收它的退出状态，进程表中残留一条死记录（不占 CPU 内存，但占 PID）。发现：ps -e -o stat,ppid,pid,cmd | grep '^Z' 或 top 里 zombie 计数。处理：杀掉它的父进程，让 init 接管回收；根因是父进程代码没调用 wait()，属于代码问题。

### 20. 后台运行命令
- tags: 进程, 实用
- difficulty: easy
- frequency: 中高频
- prompt: 怎么让命令在退出终端后继续运行？
- answer: nohup command &——nohup 忽略挂断信号，& 放后台，输出默认写 nohup.out。配合：jobs 看后台任务、fg 调回前台、screen/tmux 建会话（断线可重连）。测试场景：在服务器上跑长时间压测脚本，必须用 nohup 或 tmux，否则 SSH 一断脚本就死。

### 21. 怎么查看历史命令
- tags: 基础
- difficulty: easy
- frequency: 中高频
- prompt: 怎么快速找到并复用之前执行过的命令？
- answer: history 看历史列表；Ctrl+R 输入关键词反向搜索回车执行；!! 重复上一条命令；history | grep keyword 找包含关键词的历史。排查问题时经常要重复执行同一条观察命令，Ctrl+R 是效率神器。

### 22. 定时任务怎么配置
- tags: crontab, 实用
- difficulty: medium
- frequency: 中高频
- prompt: 怎么配置一个每天凌晨 2 点执行的定时任务？
- answer: crontab -e 编辑，写入 0 2 * * * /path/to/script.sh。五段含义：分 时 日 月 周。常用：*/5 * * * * 每5分钟；0 2 * * 1 每周一凌晨2点。注意：脚本要写绝对路径、要有可执行权限、输出建议重定向到日志方便排查"任务到底跑没跑"。

### 23. 压缩和解压命令
- tags: 基础
- difficulty: easy
- frequency: 中高频
- prompt: tar 压缩和解压的常用写法？
- answer: 压缩：tar -czvf logs.tar.gz /var/log（c 创建、z gzip、v 显示过程、f 文件名）；解压：tar -xzvf logs.tar.gz -C /target（-C 指定目录）。zip/unzip 处理 .zip 文件。记忆：**压 c 解 x**，其他参数不变。

### 24. 远程拷贝和登录命令
- tags: 网络, 实用
- difficulty: easy
- frequency: 中高频
- prompt: 怎么在服务器之间传文件和远程登录？
- answer: ssh user@host 远程登录；scp file user@host:/path 传单文件，scp -r 传目录；rsync -avz 更高效（增量传输、断点续传），大文件优先 rsync。免密登录：ssh-keygen 生成密钥后 ssh-copy-id user@host，自动化脚本里必备。

### 25. 怎么查看系统日志
- tags: 日志, 必考
- difficulty: medium
- frequency: 高频
- prompt: Linux 下怎么查看服务和系统日志？
- answer: 应用日志：tail -F /var/log/xxx.log 实时看 + grep 过滤；系统服务：systemctl status nginx 看状态，journalctl -u nginx -e 看该服务详细日志，journalctl --since "10 min ago" 看最近10分钟；内核/硬件：dmesg 或 /var/log/messages（CentOS）/var/log/syslog（Ubuntu）。排查思路：先应用日志再系统日志再内核日志。

### 26. vmstat 和 iostat 是干什么的
- tags: 监控, 加分
- difficulty: medium
- frequency: 加分题
- prompt: vmstat 和 iostat 分别能看什么？
- answer: vmstat 1 每秒刷新系统概况：r（就绪队列，超核数说明 CPU 忙）、si/so（swap 换入换出，非 0 说明内存不足）、bi/bo（磁盘块读写）、wa（IO 等待）。iostat -x 1 看磁盘详情：%util（接近 100% 磁盘饱和）、await（IO 平均耗时毫秒）。排查磁盘瓶颈的标准组合。

### 27. iowait 高说明什么
- tags: 监控
- difficulty: medium
- frequency: 中高频
- prompt: top 里 wa（iowait）很高说明什么问题？
- answer: wa 高表示 CPU 空闲着在等磁盘 IO 完成——瓶颈在磁盘不在 CPU。常见原因：数据库大量读写、日志刷盘太猛、磁盘故障慢。下一步用 iostat -x 1 确认磁盘 %util 和 await，再用 iotop 找到 IO 最重的进程。加分点：加内存缓存、换 SSD、优化 SQL 都是解法。

### 28. load average 怎么判断系统过载
- tags: 监控
- difficulty: medium
- frequency: 中高频
- prompt: load average 三个值怎么解读？多高算过载？
- answer: 三个值是 1/5/15 分钟的平均负载（正在运行+等待运行+不可中断睡眠的进程数）。判断标准：**负载超过 CPU 核数就是过载**——4 核机器 load 4.0 就是满负荷，超过 4 就有任务在排队。看趋势：1 分钟值 > 15 分钟值说明负载正在上涨，反之在回落。加分点：D 状态（不可中断 IO）也会计入 load，所以 load 高不一定是 CPU 不够。

### 29. 怎么看某个进程打开了哪些文件
- tags: 排查, 加分
- difficulty: medium
- frequency: 中高频
- prompt: 怎么查看进程打开了哪些文件？怎么找"已删除但仍占空间"的文件？
- answer: lsof -p PID 看进程打开的所有文件（日志、socket、库）；lsof -i :8080 看端口占用；经典场景：磁盘满但找不到大文件时，lsof +L1 或 lsof | grep deleted 找"已删除但仍被进程持有"的文件——rm 后进程没释放句柄，空间不返还，重启进程或 truncate 才能释放。

### 30. 环境变量相关命令
- tags: 基础
- difficulty: easy
- frequency: 中高频
- prompt: 怎么查看和设置环境变量？怎么永久生效？
- answer: 查看全部：env 或 printenv；查看单个：echo $PATH；临时设置：export MY_VAR=hello（只对当前会话生效）；永久生效：写入 ~/.bashrc（当前用户）或 /etc/profile（全系统），然后 source ~/.bashrc 立即加载。测试场景：JDK、Python 虚拟环境、接口测试的 base_url 常用环境变量管理。

### 31. 怎么测试网络连通性
- tags: 网络, 必考
- difficulty: easy
- frequency: 高频
- prompt: 怎么判断两台机器/服务之间网络通不通？
- answer: 分层排查：ping ip 测底层连通（注意禁 ping 不代表服务挂）；telnet ip port 或 curl -v ip:port 测端口通不通（测试环境最常用）；curl -I url 看 HTTP 响应头；nslookup/dig 域名 确认 DNS 解析是否正常；traceroute 看路径哪一跳断了。记忆：**ping 测机器、telnet/curl 测服务、dig 测解析**。

### 32. ss/netstat 查看网络连接
- tags: 网络
- difficulty: easy
- frequency: 中高频
- prompt: 怎么查看当前有哪些网络连接和监听端口？
- answer: ss -lntp 查看监听端口和对应进程（l 监听、n 数字显示、t TCP、p 进程）；ss -ant 查看所有 TCP 连接状态（可数 ESTABLISHED/CLOSE_WAIT）；netstat 是老命令功能相同。测试场景：验证服务是否起来、看压测时的连接数分布、CLOSE_WAIT 堆积说明程序没正确关闭连接。

### 33. curl 和 wget 的区别
- tags: 网络
- difficulty: easy
- frequency: 中高频
- prompt: curl 和 wget 有什么区别？分别什么时候用？
- answer: curl 偏"调试接口"：支持各种 HTTP 方法、自定义 header、只看响应头（curl -I）、返回内容直接打到终端，适合测试调接口；wget 偏"下载文件"：递归下载、断点续传、后台下载，适合拉包拉文件。一句话：**curl 调接口，wget 下文件**。

### 34. vi 编辑文件的常用操作
- tags: 基础, 实用
- difficulty: easy
- frequency: 中高频
- prompt: 在服务器上用 vi 改配置文件的基本操作？
- answer: vi file 打开 → i 进入编辑模式改内容 → Esc 退出编辑 → :wq 保存退出（:q! 不保存强退）。高频快捷键：/keyword 搜索、n 下一个匹配、gg 回文件头、G 到文件尾、dd 删行、u 撤销。测试场景：临时改 hosts、改配置重启服务。

### 35. 怎么比较两个文件的差异
- tags: 文本处理
- difficulty: easy
- frequency: 中高频
- prompt: 怎么比较两个文件/目录的差异？
- answer: diff file1 file2 看差异；diff -r dir1 dir2 递归比较目录（测试常用：对比两个环境的配置目录）；vimdiff 彩色对比更直观。场景：发版前后配置比对、测试数据比对。

### 36. 怎么统计文件/目录大小
- tags: 基础
- difficulty: easy
- frequency: 高频
- prompt: 怎么查看文件、目录和整个磁盘的使用情况？
- answer: ls -lh file 看单文件大小；du -sh dir 看目录总大小（-s 汇总）；du -h --max-depth=1 / | sort -hr 逐层找大目录；df -h 看磁盘分区整体使用率。排查磁盘满时的标准组合。

### 37. 怎么找出最近修改过的文件
- tags: 查找, 实用
- difficulty: easy
- frequency: 中高频
- prompt: 怎么找出最近 3 天内修改过的日志文件？
- answer: find /var/log -name "*.log" -mtime -3 ——mtime -3 表示 3 天内修改过；-mtime +7 表示 7 天前；-mmin -60 表示 60 分钟内。测试场景：排查"配置是谁什么时候改的"、清理过期日志都靠它。

### 38. 如何查看一个服务的状态和启动失败原因
- tags: 服务管理, 必考
- difficulty: medium
- frequency: 高频
- prompt: 服务启动失败了，怎么查原因？
- answer: ① systemctl status nginx 看状态和最后几行错误；② journalctl -u nginx -e 看该服务完整日志（-e 跳到结尾）；③ journalctl -u nginx --since "10 min ago" 限定时间范围；④ 再看应用自身日志。思路：先 status 定位现象，再 journalctl 挖细节。

### 39. PATH 的作用
- tags: 基础
- difficulty: easy
- frequency: 中高频
- prompt: PATH 环境变量是干什么的？为什么有时命令找不到？
- answer: PATH 是命令搜索路径列表——执行命令时系统按 PATH 里的目录顺序找可执行文件。报 command not found 通常就是：命令不在 PATH 里、没装、或没有执行权限。解决：which cmd 确认位置，export PATH=$PATH:/new/dir 追加路径。测试场景：自研测试工具要加进 PATH 才能全局调用。

### 40. 如何批量重命名或批量处理文件
- tags: 实用, 脚本
- difficulty: medium
- frequency: 加分题
- prompt: 怎么批量处理文件，比如把所有 .txt 改成 .bak？
- answer: 思路一：for f in *.txt; do mv "$f" "${f%.txt}.bak"; done（${f%.txt} 去掉后缀）。思路二：find + -exec：find . -name "*.log" -mtime +7 -exec rm {} \; 删 7 天前日志。思路三：复杂逻辑写 Python 脚本更清晰。加分点：批量操作前先 ls 预览一遍要处理的文件，确认无误再执行，防止误删。
