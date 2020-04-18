## monky

monky 是用于Android 手机应用的压力测试 

monky :Android自带工具----/system/framework/monky.jar



### monky执行:

```
adb shell monky -p com.android.settings(包名) 100(操作次数) > log存储路径
```

#### 1. 参数 -v (日志详细等级):

```
adb shell monky -p com.android.settings(包名) -v 100(操作次数) > log存储路径
```

```
adb shell monky -p com.android.settings(包名) -v -v 100(操作次数) > log存储路径
```

```
adb shell monky -p com.android.settings(包名) -v  -v -v 100(操作次数) > log存储路径
```

#### 2.参数 -s :指定 伪随机种子 (再运行时传入相同种子会执行相同的操作--动作和顺序)

```
adb shell monky -p com.android.settings(包名) -v -v -s 10(伪随机种子) 100(操作次数) > log存储路径
```

#### 3.参数  --throttle :动作执行间隔时间(毫秒)  

~~~
adb shell monky -p com.android.settings(包名) -v -v --throttle 5000 -s 10(伪随机种子) 100(操作次数) > log存储路径
~~~

#### 4.日志分析:

##### 设置相关执行概率 加参数:

~~~
--pct-touch <percent>  :触摸事件
~~~

~~~
--pct-motion <percent>  :调整动作事件
~~~

~~~
--pct-trackball <percent>   :调整轨迹事件
~~~

~~~
--pct-nav <percent>   :调整"基本"导航事件
~~~

~~~
--pct-majornav <percent>   :调整"只要"导航事件
~~~

~~~
--pct-syskeys <percent>   :调整系统按键事件
~~~

~~~
--pct-appswich <percent>   :调整启动activity 的百分比
~~~

~~~
--pct-anyevent <percent>   :调整其他随机事件的百分比
~~~

5.monky 执行结果:

​			正常:

~~~
//monky finished
~~~

​			异常:

~~~
程序无响应:日志中搜索  "ANR"  查看信息
~~~

~~~
程序崩溃:日志中搜索  "Exception"\"Crashes"\"error"  查看信息   --空指针异常 (NullpointerException)---复制 伪随机种子(seed)再执行
~~~

