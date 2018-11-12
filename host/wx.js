Array.prototype.remove = function(s) {
    for (var i = 0; i < this.length; i++) {
        if (s == this[i]) this.splice(i, 1);   //  删除指定的key
    }
}

function Map1() {

    this.keys = new Array();
    
    this.data = new Object();

    this.put = function(key, value) {
        if (this.data[key] == null) {
            this.keys.push(key);      //  若是没有key  则加入到keys  做事存在 就=value
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
    //  entrys 函数：
    this.entrys = function() {
        var len = this.keys.length;    // 将keys 和对应的value 复制到了entrys中
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
  //   获取 排名的函数
  var famous = function(val) {
  var rank;
  var unfamous_num=0;
     $.ajax({
     	type:"GET",
     	url:"http://data.alexa.com/data/?cli=10&dat=snba&ver=7.0&url="+val,
     	dataType:"xml",
     	success:function(xml){
           rank=$(xml).find("ALEXA SD POPULARITY").attr("TEXT"); //  排名 
           console.log(rank)
	       if(rank>1000||rank==undefined){
                unfamous_num = 1;
	       }else{
                unfamous_num = 0;
           }
           
           console.log(unfamous_num);
           return unfamous_num;
         }
         
      })
     	   
    }
//  判断存在1次,或者2次的host 是否在alex排a 的名种
var action =function() {
    var hanjian_host_num =  0 ;
    var es = m.entrys();
    var aa=0;
    var flag = false;
    for (var i = 0; i < es.length; i++) {
        var e = es[i];
        if ((e.value == 1||e.value==2)) {
            var k=e.key;
            var splitgroup=k.split(".");
            var shuzi=splitgroup.pop();
        	if(isNaN(shuzi)==true){
            aa = famous(e.key);
        	hanjian_host_num = hanjian_host_num + aa;
        	}
            }else{
            hanjian_host_num =hanjian_host_num + 0;
        }
    }
    return hanjian_host_num
}

    var s=0;
    var m = new Map1(); // 定义了一个数据结构
    var cururl;
    var externlink=0;
    var internlink=0;
    var sunLink;
    var bili;

    chrome.webRequest.onBeforeSendHeaders.addListener(function(details) { 
        s=s+1;  // 发送的请求数目 
        var url = details.url;
        strs = url.split("/");
        host = strs[2];
        var flag = false;
        var split = host.split(".");
        var len=split.length;
        var rule="";
        erji=split.pop();
        yiji=split.pop();
        rule=yiji+"."+erji;
        if (s==1){
            viewUrl=rule;
        }
        var es = m.entrys(); //。。{baidu.com: 282, bdstatic.com: 145, com.hk: 2, alexa.com: 11, xrcch.com: 2, …}
        for (var i = 0; i < es.length; i++) {
            var e = es[i];
            if (rule == e.key) {    //当前监听的host是否==e.key    =key   次数加一 跳出  不等于key 就继续循环
                flag = true;
                break;
             }
        }
        if (flag == false) {
            m.put(rule, 1);    //  key 出现的次数
        } else {
            m.put(rule, m.get(rule) + 1);    //  出现次数+1
        }
      },
     {
        urls: ["<all_urls>"]   //过滤 URL 选择
       },
       ["requestHeaders", "blocking"]);


    chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
       
    if(changeInfo.status=='loading'){
        m = new Map1();
        externlink=0;
        internlink=0;
        sunLink=0;
        bili = 0;
     }  // loading...

     if(changeInfo.status=='complete'){
        if(tab.url=='chrome://newtab/'){

        }else{
           cururl=tab.url;
           
  		   curstrs = cururl.split("/");
           curhost = curstrs[2];// console.log(curhost)     www.baidu.com
           var cursplit = curhost.split(".");   //     ['www','baidu','com']
           var len=cursplit.length;  // 3 
           var cur="";     
           erji=cursplit.pop();  // com
           yiji=cursplit.pop();   // baidu
           cur=yiji+"."+erji;   // baidu.com
           var es = m.entrys(); // [ 'baidu.com','bdstatic.com']
     
         // 内外链接
         for (var i = 0; i < es.length; i++) {
           var e = es[i];
           if (cur == e.key) {
                internlink= e.value;
            }else{
              	externlink=externlink+e.value-1 ;
             }
          }

        //获取罕见host的数目
         hj_host_num=action()
        // 请求总数
         var req_type_num =es.length 
         //内外请求
         var sumLink=internlink+externlink;
         var bili = internlink/sumLink;
         var result = curhost+','+internlink+','+externlink+','+sumLink+','+bili +','+req_type_num+','+hj_host_num; 
         
         cur='http://'+ curhost    // 修改。
         console.log(JSON.stringify({url:cur,neiwai:[internlink,externlink,sumLink,bili,req_type_num,hj_host_num]}))
         var data1=JSON.stringify({url:cur,neiwai:[internlink,externlink,sumLink,bili,req_type_num,hj_host_num]})
        //  var data1 =JSON.stringify({data : m.data})
                $.ajax({
                    type:"POST",
                    url:'http://localhost:2222/test',
                    data:data1,
                    contentType: "application/json; charset=utf-8",  
                    dataType: "json",
                    success: function(data) { 
                    if(data['res']==0){
                        alert('this webpage is safety');
                    }else{
                        alert('this webpage is malicious');
                     }                 
                   } 
                });
            } 
        }
      
    })
   