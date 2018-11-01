Array.prototype.remove = function(s) {
    for (var i = 0; i < this.length; i++) {
        if (s == this[i]) this.splice(i, 1);
    }
}

// define class 
function Map1() {
    // 属性
    this.keys = new Array();
    this.data = new Object();
    // 方法
    this.put = function(key, value) {
        if (this.data[key] == null) {
            this.keys.push(key);
        }
        this.data[key] = value;
    };

    this.get = function(key) {
        return this.data[key];
    };

    this.remove = function(key) {
        this.keys.remove(key);
        this.data[key] = null;
    };

    this.each = function(fn) {
        if (typeof fn != 'function') {
            return;
        }
        var len = this.keys.length;
        for (var i = 0; i < len; i++) {
            var k = this.keys[i];
            fn(k, this.data[k], i);
        }
    };

    this.entrys = function() {
        var len = this.keys.length;
        var entrys = new Array(len);
        for (var i = 0; i < len; i++) {
            var tmp = this.keys[i];
            entrys[i] = {
                key: tmp,
                value: this.data[tmp]
            };
        }
        return entrys;
    };

    this.isEmpty = function() {
        return this.keys.length == 0;
    };

    this.size = function() {
        return this.keys.length;
    };

    this.toString = function() {
        var s = "{";
        for (var i = 0; i < this.keys.length; i++, s += ',') {
            var k = this.keys[i];
            s += k + "=" + this.data[k];
        }
        s += "}";
        return s;
    };
}

    function famous(val) {
     var rank; 
     $.ajax({
     	type:"GET",
     	url:"http://data.alexa.com/data/?cli=10&dat=snba&ver=7.0&url="+val,
     	dataType:"xml",
     	success:function(xml){
	       rank=$(xml).find("ALEXA SD POPULARITY").attr("TEXT");
	       console.log(rank);
	       if(rank>1000||rank==undefined){
	           var percentcdx;var gailvcdx;
			   percentcdx=redirectnum/sum;
	           if(percentcdx>=0.05){
	               gailvcdx=1;
	           }else if(percentcdx<=0.02){
	               gailvcdx=0;
	           }else{
	               gailvcdx=(percentcdx*100-2)/3;
	           }
	           var percentdiaoyu;var gailvdaioyu;
			   percentdiaoyu=externlink/(externlink+internlink);
	           if(percentdiaoyu>=0.75){
	               gailvdaioyu=1;
	           }else if(percentdiaoyu<=0.25){
	               gailvdaioyu=0;
	           }else{
	               gailvdaioyu=(percentdiaoyu*100-25)/50;
	           }
               console.log("web page is suspicious and the possibility of redirect is "+(gailvcdx*100).toFixed(2)+"%, the possibility of diaoyu is "+(gailvdaioyu*100).toFixed(2)+"%");
	           alert("web page is suspicious and the possibility of redirect is "+(gailvcdx*100).toFixed(2)+"%, the possibility of diaoyu is "+(gailvdaioyu*100).toFixed(2)+"%");
	       
	       }



     	}


     })
     	      


	}



var action =function() {
    var es = m.entrys();
    var flag = false;
    for (var i = 0; i < es.length; i++) {
        var e = es[i];
        if ((e.value == 1||e.value==2)) {
        	var k=e.key;
        	var splitgroup=k.split(".");
        	var shuzi=splitgroup.pop();
        	if(isNaN(shuzi)==true){

        	  famous(e.key);

        	}

        }
    }

}

  

	// var sum=0;
	// var redirectnum = 0;
    // chrome.webRequest.onHeadersReceived.addListener(function(details) {

    //     sum = sum + 1;
    //     if (details.statusCode == 301 || details.statusCode == 302|| details.statusCode == 303|| details.statusCode == 304|| details.statusCode == 305|| details.statusCode == 300) {
    //         redirectnum = redirectnum + 1;

    //     }

    // },

    // {
    //     urls: ["<all_urls>"]
    // },
    // ["responseHeaders", "blocking"]

    // );

    var cururl;
    var externlink=0;
    var internlink=0;
    chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
   
        if(changeInfo.status=='complete'){
            var s=0;
            var m = new Map1(); 
            // 监听网页。
            chrome.webRequest.onBeforeSendHeaders.addListener(function(details) {
                s=s+1;
                var url = details.url;
        //         console.log(url);
                strs = url.split("/");
                host = strs[2];
                var flag = false;
                var split = host.split(".");
                var len=split.length;
                var rule="";
                erji=split.pop();
                yiji=split.pop();
                rule=yiji+"."+erji;
                var es = m.entrys();// 调用类中的方法
                for (var i = 0; i < es.length; i++) {
                    var e = es[i];
                    if (rule == e.key) {
                        flag = true;
                        break;
                    }
                }
                if (flag == false) {
                    m.put(rule, 1);
                } else {
                    m.put(rule, m.get(rule) + 1);
                }   //  构建Map。。。。。。
            },
        
            {
                urls: ["<all_urls>"]
            },
            ["requestHeaders", "blocking"]
        
            );
            console.log(m);
        //   if(changeInfo.url=='chrome://newtab/'){
            // 访问网页
            // cururl=tab.url;
            // curstrs = cururl.split("/");
            // curhost = curstrs[2];
            // var cursplit = curhost.split(".");
            // var len=cursplit.length;
            // var cur="";
            // erji=cursplit.pop();
            // yiji=cursplit.pop();
            // cur=yiji+"."+erji;  // baidu.com
            //   var es = m.entrys();
            //   console.log(es)
        //     for (var i = 0; i < es.length; i++) {
        //         var e = es[i];
        //     if (cur == e.key) {
        //     	internlink=internlink+1;

        //     }else{
        //     	externlink=externlink+1;
        //     }
        // }

   
        }

	
         
        //  if (changeInfo.status == "complete") 
        //       action();
        
    })