// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://wsdx.ustc.edu.cn/ybdy/play*
// @icon         https://www.google.com/s2/favicons?domain=ustc.edu.cn
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    function GetQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    console.log(window.location.search)//?id=2
    console.log(window.location)
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}

     function start() {

        var video = document.getElementById("video");
        //处理播放器事件
        if (video) {
            $("public_submit").trigger("click");
             $("public_cancel").trigger("click");

            let playerH5 = document.getElementById("video");
            if (playerH5.paused) {
                console.log("123");
                $("public_submit").trigger("click"); //此为关闭方法
                $(".public_close").trigger("click");
                playerH5.play();
            }
            video.addEventListener('pause', function () { //开始执行的函数
                console.log("播放结束");
                 var rid = GetQueryString("r_id");
                 var vid = GetQueryString("v_id");
                rid = parseInt(rid)
                rid = rid +1
                console.log(vid,rid);


    });
            video.addEventListener('ended', function () { //开始执行的函数
                console.log("播放结束");
                 var rid = GetQueryString("r_id");
                 var vid = GetQueryString("v_id");
                rid = parseInt(rid)
                rid = rid +1
                console.log(vid,rid);
                window.location.href="http://wsdx.ustc.edu.cn/ybdy/play?v_id="+vid+"&r_id="+rid+"&r=video"


    });

        }
        setTimeout(start,10000);
     }
    console.log("脚本加载正常");
    setTimeout(start, 3000);

    // Your code here...
})();