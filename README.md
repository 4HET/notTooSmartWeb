## 写在开始

本项目为作者的安卓实训webview的后端部分，本项目仅供学习使用，若有侵权联系作者删除

## 开发目的

在上课我们需要查看课表，以便知道去哪个教室时，我们需要打开智慧曲园或者掌上曲园公众号进行查询，步骤繁琐且等待时间长（一套操作下来至少十几秒），严重影响用户体验，因此我想能不能自己开发一个app来简化这些操作，因此第一个功能——课表功能便产生了。该功能是为了用户能够在上课途中快速查询课表使用

现在疫情形势不容乐观，我们需要每天在智慧曲园上传自己的健康信息，但是有时候我们的身体并没有出现一样并且也一直保持“校区园区，两点一线“，这时打卡上传就显得有点”繁琐“，因此第三个功能——自动打卡便产生了，该功能可以辅助用户进行自动打卡，若用户身体出现异样，则应该即时停止自动打卡功能，于智慧曲园如实填报

## 应用功能

### 登录功能

本校学生可以通过自己的智慧曲园账号密码登录该软件（无需注册且只能通过智慧曲园账号密码登录），登录默认保存账号密码，以便在下次登录时直接跳转到主界面，省去输入账号密码的时间，更加方便日常使用

### 课表功能

使用自己的智慧曲园账号密码登录后，可以看到自己的课表（目前设置金可查看当周课表），可以显示上课科目、上课时间、上课教室这三模块内容

### 成绩功能

使用自己的智慧曲园账号密码登录后，可以查看自己的成绩，包括考试科目、考试成绩、绩点、对应科目学分，后续可能会再开放四六级成绩查询功能，想要使用的用户需要输入自己的身份证号

### 自动打卡功能

该功能为选择性功能，即用户可以选择不使用：若用户身体状况很好可以选择使用该功能自动上传打卡数据，若身体情况不好，还应使用智慧曲园如实填报。使用该功能的用户，会于第二天随机时间自动打卡。用户可以选择打卡成功后的提示功能，若选择该功能，需要提供自己的邮箱，打卡成功后会将打卡成功信息信息发送至你提供的邮箱，发送信息支持自定义。


## 技术实现

本项目（webview的后端）使用前端Vue+Element UI+h5，后端Django+python爬虫，数据库MySQL进行技术实现，用户既可以通过按住访问，也可直接通过web访问

### 登录检测

通过java网络编程技术，每次用户登录，向智慧曲园发送网络请求，根据智慧曲园的响应体信息判断用户名是否存在，密码是否正确。若密码正确，则使用```SharedPreferences```
保存密码，保存密码后下一次登录无需输入，直接跳转到主界面

### 实现android与html通信的方法：

使用```webView.addJavascriptInterface```，该方法允许向js页面注入java对象

在安卓中，通过以下代码向JavaScript注入Java类

```java
webView.addJavascriptInterface(PunchActivity.this, "getUsername");
webView.addJavascriptInterface(PunchActivity.this, "getPassword");

@JavascriptInterface
public String getPassword() {
    Log.i("inputPassword", "js接受了来自安卓的密码");
    return inputPassword;
}

@JavascriptInterface
public String getUsername() {
    Log.i("inputUsername", "js接受了来自安卓的用户名");
    return inputUsername;
}
```

在html中，使用一下代码接收数据：

```html

<div id="username" onclick="getAndroidUsername()" style="width:100px; height:100px; background-color:#000899;"></div>
<script type="text/javascript">

    function getAndroidUsername() {
        document.getElementById("username").innerHTML = window.getUsername.getUsername();
    }

</script>
<div id="password" onclick="getAndroidPassword()" style="width:100px; height:100px; background-color:#099;"></div>
<script type="text/javascript">
    function getAndroidPassword() {
        document.getElementById("password").innerHTML = window.getPassword.getPassword();
    }
</script>
```

### Vue前端开发

前端使用Vue进行开发，引入element ui模块使开发更加迅速，使界面更加简洁美观，避免“造轮子”而浪费时间，把时间放在Android开发与Django开发，使后端的开发更加的简洁；使用浮动框架，标题导航栏作为主界面，各个应用嵌入主界面，在点击相应的栏目，内容部分会跳转到相应的界面。

当前端检测到登陆数据来自Android时，调用js方法自动填充密码并且点击登录；当检测到数据是来自web时，会让用户自己选择输入密码进行登录

```javascript
<script>
    window.onload = to_punch;
    function to_punch() {
        // document.getElementById("ifr").setAttribute("src", "../punch")
        try {
            document.getElementById("username").value = window.getUsername.getUsername();
            document.getElementById("password").value = window.getPassword.getPassword();
            document.getElementById("myForm").submit();
        } catch (err) {
            document.getElementById("username").value = "";
            document.getElementById("password").value = "";
            // document.getElementById("myForm").submit();
        }
    }

</script>
```

### Django后端开发

在web开发中，后端使用Django的MTV三层架构，应用之间相互独立，易于维护；使用mysql数据库技术，将用户信息存下，方便后端进行打卡自动化以及服务的提供。用户必须登录后才可访问具体界面，若用户直接访问成绩、打卡界面，系统会重定向到登陆界面。
### python爬虫

用户登录后，对应的app调用相应的爬虫程序，对智慧曲园课表、成绩进行爬取，再将数据交由后端格式化数据，最终将格式化的数据返回到前端通过Vue进行显示

### mysql数据库

数据库负责授权用户：当用户想使用时需要联系作者在数据库进行授权，授权后可进行登陆查看自己的课表、成绩以及自动打卡信息。打卡界面用户可以选择输入自己的邮箱，打卡成功或失败后系统会发邮件到用户的邮箱。
