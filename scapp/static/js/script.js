$(document).ready(function(){
		$('tr:odd').addClass('odd');
		$('tr:even').addClass('even')
	});
// 动态创建表单
function createForm(action,arr){
    var tmpForm = $("<form action='"+action+"' method='POST'></form>");
    for(var key in arr) {
        tmpForm.append("<input type='hidden' value='"+arr[key]+"' name='"+key+"'/>");
    }
    tmpForm.appendTo(document.body).submit();
}

function submitForm(formId,action){
    document.getElementById(formId).action = action;
    document.getElementById(formId).submit();
}

function creattime(i){
    if(i<10)
        {i="0"+i};
    return i;
}
var date=new Date();
var year=date.getFullYear();
var month=creattime(date.getMonth()+1);
var day=creattime(date.getDate()); 
//日历
function datepicker(){
    $('.datepicker').datepicker();
    //给空的datepicker一个默认当天值
    $('.datepicker').each(function(){
        if(this.value==""){
            this.value=year+"-"+month+"-"+day;
        }
    });
    // if($('.datepicker').val()==""){
    //     var date=new Date();
    //     var nian=date.getFullYear();
    //     var month=creattime(date.getMonth()+1);
    //     var day=creattime(date.getDate()); 
    //     function creattime(i){
    //         if(i<10)
    //             {i="0"+i};
    //         return i;
    //     }
    //     $('.datepicker').val(nian+"-"+month+"-"+day);
    //     alert($('.datepicker').length)

    // }
    
		// var dateFormat = $('.datepicker').datepicker('option', 'dateFormat');
		// $('.datepicker').datepicker({ dateFormat: 'yy-mm-dd' });		
		// $('.datepicker').datepicker('option', 'dateFormat', 'yy-mm-dd');		
}

//iframe自适应高度用于iframe内部页面			
function Frame(){
	var content_iframe = $('#content_frame',window.parent.document);//获取iframeID
    var height = parseInt($(".content").height())+60;//使iframe高度等于子网页高度	
    content_iframe.height ( height < 500 ? 500 : height);
}

//iframe自适应高度用于主页面
function resizeFrame(id){
	var height = $('#'+id).contents().find(".content").height();
    if(id=="content_frame"){        
        $('#'+id).height( height < 500 ? 500 :height+60);
    }
    else{
        $('#'+id).height(height+60);
    }
    
    //if(id=='content_frame')
	   //$('#'+id).height(height < 500 ? 500 : height+40);
   // else
       //$('#'+id).height(height+20); 
}

//左侧leftmenu样式变换
function leftmenu(obj){
	var leftmenu=$("li[id]")//*注意IE6不识别属性选择器*
	for(i=0;i<leftmenu.length;i++)
		leftmenu[i].className="";
	obj.className="active";	
}

//切换iframe里的内容用于主页面
function changeiframe(page){
	$("#content_frame").attr("src",page);
}

//切换iframe里的内容用于iframe内部页面	
function iframe(page){
	window.location.href = "/" + page;
   // alert(window.location.href);
}

//切换iframe里的内容用于二级iframe内部页面  
function doubleiframe(page){
    window.parent.window.location.href = "/" + page;   
}

//选中表格行
function changeColor(obj){
    if(obj.checked==true)
        obj.parentElement.parentElement.style.background="#def0d8"
    else
        obj.parentElement.parentElement.style.background="#efefef"
}

//反选按钮
function ChkAllClick(){
    var arrSon = document.getElementsByName("checkbox");
    for(i=0;i<arrSon.length;i++) {
        if(arrSon[i].checked!=true)
            arrSon[i].click();
        else
            arrSon[i].click();
    }
}

/**
 * 消息闪现
 */
function setTimeOut(){
    setTimeout(function(){
        $(".alert-success").fadeOut("slow");
        $(".alert-error").fadeOut("slow");
    },3000)
}

/**
 * 显示时间
 */
function showdate()
{
    var day1=date.getDay();
    var txt;
    switch(day1)
    {
        case 1:
            txt="一"
            break
        case 2:
            txt="二"
            break
        case 3:
            txt="三"
            break
        case 4:
            txt="四"
            break
        case 5:
            txt="五"
            break
        case 6:
            txt="六"
            break
        case 0:
            txt="日"
            break
        default:
            sj.innerHTML="出错了"
    }
    document.getElementById('date').innerHTML=year+"年"+month+"月"+day+"日&nbsp;&nbsp;&nbsp;星期"+txt
}

//tab标签页
function selectTag(showContent,selfObj){
	// 操作标签
	var tag = document.getElementById("tags").getElementsByTagName("li");
	var taglength = tag.length;
	for(i=0; i<taglength; i++){
		tag[i].className = "";
	}
	selfObj.parentNode.className = "selectTag";
	// 操作内容
	for(i=0; j=document.getElementById("tagContent"+i); i++){
		j.style.display = "none";
	}
	$("#"+showContent).show();
    Frame();
}
function tab(showContent,id,selfObj){    
    var tag = document.getElementById(id).getElementsByTagName("li");
    var taglength = tag.length;
    for(i=0; i<taglength; i++){
        tag[i].className = "";
    }
    selfObj.parentNode.className = "selectTag";
    $('.tab').hide();
    $('#'+showContent).show();
}
function thirdTb(showContent,id,selfObj){    
    var tag = document.getElementById(id).getElementsByTagName("li");
    var taglength = tag.length;
    for(i=0; i<taglength; i++){
        tag[i].className = "";
    }
    selfObj.parentNode.className = "selectTag";
    $('.thirdTb').hide();
    $('#'+showContent).show();
}
//控制div的显示和隐藏
function changeDiv(show_div,hide_div){
    $("#"+show_div).show();
    $("#"+hide_div).hide();
    Frame();
}

//信贷员搜索用来赋值
function get_name(obj,idText,idValue){
    var tr=obj.parentElement.parentElement
    var td=tr.getElementsByTagName("td");
    $("#" + idText).val(td[2].innerHTML);
    $("#" + idValue).val(td[1].innerHTML);
    $(".display-div").hide(); 
}
//验证字符长度：id(验证的input)，spry(input所在的spry的id)，length(不得超过的长度)
function spryMaxLengthID(id,spry,length) {
    //存放字符串长度的结果
    var sum = 0;
    //获得用户输入的字符串
    var userInputString = document.getElementById(id).value;            
    //前256是ascii码也是Unicode（英文）
    for (var i = 0; i < userInputString.length; i++) {
        if ((userInputString.charCodeAt(i) >= 0) && (userInputString.charCodeAt(i) <= 255)) {
            sum = sum + 1;//英文就加1
        } else {
            sum = sum + 2;//除英文之外加2
        }
    }
    if(sum > length){//超出               
        $("#"+spry+" span.errorInfo").show();
        $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
    }
    else{//未超出
        $("#"+spry+" span.errorInfo").hide();
        $("input[type=submit]").removeAttr("disabled");//解除禁用提交按钮
    }
}
//双层Iframe内部
function doubleIframe(frameid){
    var content_iframe = $('#'+frameid,window.parent.document);//获取iframeID
    var height = parseInt($(".content").height())+60;//使iframe高度等于子网页高度 
    content_iframe.height(height);
    var iframe= $('#content_frame',window.parent.parent.document);
    var height1 = parseInt($(".content",window.parent.document).height())+40;
    iframe.height(height1);
}
//3层Iframe内部
function thirdIframe(parentIframe,grandIframe){
    var content_iframe1 = $('#'+parentIframe,window.parent.document);//获取iframeID
    var height1 = parseInt($(".content").height())+60;//使iframe高度等于子网页高度 
    content_iframe1.height(height1);

    var content_iframe2 = $('#'+grandIframe,window.parent.parent.document);//获取iframeID
    var height2 = parseInt($(".content").height())+60;//使iframe高度等于子网页高度 
    content_iframe2.height(height2);

    var iframe= $('#content_frame',window.parent.parent.parent.document);
    var height3 = parseInt($(".content",window.parent.parent.document).height())+40;
    iframe.height(height3);
}
//验证字符长度：obj(验证的input)，spry(input所在的spry的id)，length(不得超过的长度),错误统计max
function spryMaxLength(obj,length) {
    //获得用户输入的字符串
    var userInputString = obj.value; 
     //存放字符串长度的结果
    var sum = 0;           
    //前256是ascii码也是Unicode（英文）
    for (var i = 0; i < userInputString.length; i++) {
        if ((userInputString.charCodeAt(i) >= 0) && (userInputString.charCodeAt(i) <= 255)) {
            sum = sum + 1;//英文就加1
        } else {
            sum = sum + 2;//除英文之外加2
        }
    }
    if(sum > length){//超出  
        if($(obj).parent().find(".errorInfo").css("display")=="none")                
            max++;             
        $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
        $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
    }
    else{//未超出
        if($(obj).parent().find(".errorInfo").css("display")!="none"&&max>0)
            max--;
        $(obj).parent().find(".errorInfo").hide();  
    }
    //判断是否接触按钮禁用
    checkInput();
}
//有添加按钮的金额赋值
function setJe(obj){
    $(obj).parent().find(".je").html(hjje(obj,obj.value));
}
//金额转换大写,错误统计jegs
function hjje(obj,value){  
    //alert(obj.value);   
    var currencyDigits=value;               
    // Constants:
    var MAXIMUM_NUMBER = 99999999999.99;
    // Predefine the radix characters and currency symbols for output:
    var CN_ZERO = "零";
    var CN_ONE = "壹";
    var CN_TWO = "贰";
    var CN_THREE = "叁";
    var CN_FOUR = "肆";
    var CN_FIVE = "伍";
    var CN_SIX = "陆";
    var CN_SEVEN = "柒";
    var CN_EIGHT = "捌";
    var CN_NINE = "玖";
    var CN_TEN = "拾";
    var CN_HUNDRED = "佰";
    var CN_THOUSAND = "仟";
    var CN_TEN_THOUSAND = "万";
    var CN_HUNDRED_MILLION = "亿";
    var CN_SYMBOL = "￥";
    var CN_DOLLAR = "元";
    var CN_TEN_CENT = "角";
    var CN_CENT = "分";
    var CN_INTEGER = "整";
    // Variables:
    var integral; // Represent integral part of digit number.
    var decimal; // Represent decimal part of digit number.
    var outputCharacters; // The output result.
    var parts;
    var digits, radices, bigRadices, decimals;
    var zeroCount;
    var i, p, d;
    var quotient, modulus;
    // Validate input string:
    currencyDigits = currencyDigits.toString();
    // if (currencyDigits == "") {
    //     alert(jegs)
    //     return "还没有输入数字！";  
    // }
    // if (currencyDigits.match(/[^,.\d]/) != null) {//英文字母
    //     if($(obj).parent().find(".errorInfo").css("display")=="none")                
    //         jegs++;   
    //     alert(jegs)
    //     $(obj).parent().find(".errorInfo").show();
    //     return "请输入有效数字!";
    // }
    // if (currencyDigits != ""&&(currencyDigits).match(/^((\d{1,3}(,\d{3})*(.((\d{3},)*\d{1,3}))?)|(\d+(.\d+)?))$/) == null) {
    //     if($(obj).parent().find(".errorInfo").css("display")=="none")                
    //         jegs++;   
    //     alert(jegs)
    //     $(obj).parent().find(".errorInfo").show();
    //     return "请输入有效数字!";
       
    // }
    // Normalize the format of input digits:
    currencyDigits = currencyDigits.replace(/,/g, ""); // Remove comma delimiters.
    currencyDigits = currencyDigits.replace(/^0+/, ""); // Trim zeros at the beginning.
    // Assert the number is not greater than the maximum number.
    if ((currencyDigits != ""&&(currencyDigits).match(/^((\d{1,3}(,\d{3})*(.((\d{3},)*\d{1,3}))?)|(\d+(.\d+)?))$/) == null)||(currencyDigits.match(/[^,.\d]/) != null)){
        if($(obj).parent().find(".errorInfo").css("display")=="none")               
            jegs++;  
        $(obj).parent().find(".errorInfo").show();
        //alert(jegs);
        $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮   
        return "<font style='color:#CC3333'>请输入有效数字!</font>"; 
        //return "您输入的数字太大了!";
    }
    else{
        if(currencyDigits == ""){
            if($(obj).parent().find(".errorInfo").css("display")!="none"&&jegs>0) {               
                jegs--;   
                //alert(jegs);
                $(obj).parent().find(".errorInfo").hide(); 
            } 
            checkInput();
            return "￥";
        }
        else{

            if($(obj).parent().find(".errorInfo").css("display")!="none"&&jegs>0)                
                jegs--;   
            //alert(jegs);
            $(obj).parent().find(".errorInfo").hide();  
        }
               
    }
    // Process the coversion from currency digits to characters:
    // Separate integral and decimal parts before processing coversion:
    parts = currencyDigits.split(".");
    if (parts.length > 1) {
        integral = parts[0];
        decimal = parts[1];
        // Cut down redundant decimal digits that are after the second.
        decimal = decimal.substr(0, 2);
    }
    else {
        integral = parts[0];
        decimal = "";
    }
    // Prepare the characters corresponding to the digits:
    digits = new Array(CN_ZERO, CN_ONE, CN_TWO, CN_THREE, CN_FOUR, CN_FIVE, CN_SIX, CN_SEVEN, CN_EIGHT, CN_NINE);
    radices = new Array("", CN_TEN, CN_HUNDRED, CN_THOUSAND);
    bigRadices = new Array("", CN_TEN_THOUSAND, CN_HUNDRED_MILLION);
    decimals = new Array(CN_TEN_CENT, CN_CENT);
    // Start processing:
    outputCharacters = "";
    // Process integral part if it is larger than 0:
    if (Number(integral) > 0) {
        zeroCount = 0;
        for (i = 0; i < integral.length; i++) {
            p = integral.length - i - 1;
            d = integral.substr(i, 1);
            quotient = p / 4;
            modulus = p % 4;
            if (d == "0") {
                zeroCount++;
            }
            else {
                if (zeroCount > 0){
                    outputCharacters += digits[0];
                }
                zeroCount = 0;
                outputCharacters += digits[Number(d)] + radices[modulus];
            }
            if (modulus == 0 && zeroCount < 4) {
                outputCharacters += bigRadices[quotient];
            }
        }
        outputCharacters += CN_DOLLAR;
    }
    // Process decimal part if there is:
    if (decimal != "") {
        for (i = 0; i < decimal.length; i++) {
            d = decimal.substr(i, 1);
            if (d != "0") {
                outputCharacters += digits[Number(d)] + decimals[i];
            }
        }
    }
    // Confirm and return the final output string:
    if (outputCharacters == "") {
        outputCharacters = CN_ZERO + CN_DOLLAR;
    }
    if (decimal == "") {
        outputCharacters += CN_INTEGER;
    }
    outputCharacters = CN_SYMBOL + outputCharacters;

    checkInput();
    return outputCharacters; 
}
//验证1-100数字,错误统计num
function check(obj,min,max){    
    if(parseInt(obj.value)<min || parseInt(obj.value)>max){
        if($(obj).parent().find(".errorInfo").css("display")=="none")                
            num++;             
        $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
        $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
    }
    else{
        if($(obj).parent().find(".errorInfo").css("display")!="none"&&num>0)
            num--;
        $(obj).parent().find(".errorInfo").hide();       
    }
    checkInput();
} 
//身份证验证,错误统计idCard
function checkIdcard(obj) {
            var idcard = obj.value;           
            var area = { 11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古", 21: "辽宁", 22: "吉林", 23: "黑龙江", 31: "上海", 32: "江苏", 33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东", 41: "河南", 42: "湖北", 43: "湖南", 44: "广东", 45: "广西", 46: "海南", 50: "重庆", 51: "四川", 52: "贵州", 53: "云南", 54: "西藏", 61: "陕西", 62: "甘肃", 63: "青海", 64: "宁夏", 65: "新疆", 71: "台湾", 81: "香港", 82: "澳门", 91: "国外" }

            var idcard, Y, JYM;
            var S, M;
            var idcard_array = new Array();
            idcard_array = idcard.split("");
            /*地区检验*/
            if (area[parseInt(idcard.substr(0, 2))] == null) {
                if($(obj).parent().find(".errorInfo").css("display")=="none")                
                    idCard++;  
                    //alert(idCard)           
                $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
                $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
                return false;
            }
            /*身份号码位数及格式检验*/
            switch (idcard.length) {
                case 15:
                    if ((parseInt(idcard.substr(6, 2)) + 1900) % 4 == 0 || ((parseInt(idcard.substr(6, 2)) + 1900) % 100 == 0 && (parseInt(idcard.substr(6, 2)) + 1900) % 4 == 0)) {
                        ereg = /^[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$/;//测试出生日期的合法性
                    } else {
                        ereg = /^[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$/;//测试出生日期的合法性
                    }
                    if (ereg.test(idcard)) {
                        if($(obj).parent().find(".errorInfo").css("display")!="none"&&idCard>0)                
                            idCard--;             
                        $(obj).parent().find(".errorInfo").hide();//隐藏改文本框所在span的className为errorInfo的错误信息    
                        checkInput();//是否解除禁用提交按钮                    
                        return false;
                    }
                    else {
                        if($(obj).parent().find(".errorInfo").css("display")=="none")                
                            idCard++;             
                        $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
                        $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
                        return false;
                    }
                    break;

                case 18:
                    //18位身份号码检测
                    //出生日期的合法性检查 
                    //闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
                    //平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
                    if (parseInt(idcard.substr(6, 4)) % 4 == 0 || (parseInt(idcard.substr(6, 4)) % 100 == 0 && parseInt(idcard.substr(6, 4)) % 4 == 0)) {
                        ereg = /^[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$/;//闰年出生日期的合法性正则表达式
                    } else {
                        ereg = /^[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$/;//平年出生日期的合法性正则表达式
                    }
                    if (ereg.test(idcard)) {//测试出生日期的合法性
                        //计算校验位
                        S = (parseInt(idcard_array[0]) + parseInt(idcard_array[10])) * 7
                        + (parseInt(idcard_array[1]) + parseInt(idcard_array[11])) * 9
                        + (parseInt(idcard_array[2]) + parseInt(idcard_array[12])) * 10
                        + (parseInt(idcard_array[3]) + parseInt(idcard_array[13])) * 5
                        + (parseInt(idcard_array[4]) + parseInt(idcard_array[14])) * 8
                        + (parseInt(idcard_array[5]) + parseInt(idcard_array[15])) * 4
                        + (parseInt(idcard_array[6]) + parseInt(idcard_array[16])) * 2
                        + parseInt(idcard_array[7]) * 1
                        + parseInt(idcard_array[8]) * 6
                        + parseInt(idcard_array[9]) * 3;
                        Y = S % 11;
                        M = "F";
                        JYM = "10X98765432";
                        M = JYM.substr(Y, 1);/*判断校验位*/
                        if (M == idcard_array[17]) {
                            if($(obj).parent().find(".errorInfo").css("display")!="none"&&idCard>0)                
                                idCard--;             
                            $(obj).parent().find(".errorInfo").hide();//隐藏改文本框所在span的className为errorInfo的错误信息    
                            checkInput();//是否解除禁用提交按钮 
                            return false; /*检测ID的校验位*/
                        }
                        else {
                            if($(obj).parent().find(".errorInfo").css("display")=="none")                
                                idCard++;             
                            $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
                            $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
                            return false;
                        }
                    }
                    else {
                        if($(obj).parent().find(".errorInfo").css("display")=="none")                
                            idCard++;             
                        $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
                        $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
                        return false;
                    }
                    break;

                default:
                    if($(obj).parent().find(".errorInfo").css("display")=="none")                
                        idCard++;             
                    $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
                    $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮
                    return false;
            }
        }
//验证电话号码最少字符数,错误统计phone
function getLength(obj){
    var text="";
    text=obj.value;
    if(text.length==11||text.length==12){
        if($(obj).parent().find(".errorInfo").css("display")!="none"&&phone>0)
            phone--;
        $(obj).parent().find(".errorInfo").hide(); 
    }
    else{
        if($(obj).parent().find(".errorInfo").css("display")=="none")                
            phone++;             
        $(obj).parent().find(".errorInfo").show();//显示改文本框所在span的className为errorInfo的错误信息
        $("input[type=submit]").attr("disabled","disabled");//禁用提交按钮    
    }
    checkInput();
}

//判断是否解除按钮禁用
function checkInput(){
    if(max==0&&jegs==0&&num==0&&idCard==0&&phone==0)//max字符长度，jegs金额格式，num数字在0-100之间，idcard身份证验证
       $("input[type=submit]").removeAttr("disabled");//提交按钮解禁
}
//用来验证不可编辑的文本框
function hiddenInput(id,obj){
    $('#'+id).val(obj.value)
}
// //***************表单元素封装**********************
// function formBox(){  
// //申请信息
//     var sqxx="<table class='table-list'>"+               
//         "<tr>"+
//             "<td class='table-label'>申请金额（元）*</td>"+
//             "<td><input type='text' id=''/></td>"+
//             "<td class='table-label'>申请期限（月）*</td>"+
//             "<td><input type='text' id=''/>月</td>"+
//             "<td class='table-label'>分期还款额(元)*</td>"+
//             "<td><input type='text' id=''/></td>"   +                   
//         "</tr>"+
//         "<tr>"+
//             "<td class='table-label'>贷款用途*</td>"+
//             "<td>"+
//                 "<select>"+
//                     "<option>---请选择---</option>"+
//                     "<option>流动资金贷款</option>"+
//                 "</select>"+
//             "</td>"+
//             "<td class='table-label'>详细说明</td>"+
//             "<td colspan='3'><input type='text' id='' class='long'/></td>"+               
//         "</tr>"+
//         "<tr>"+
//             "<td class='table-label'>贷款原因</td>"+
//             "<td colspan='5'><input type='text' id='' class='long'/></td>"+                           
//         "</tr>"+
//     "</table>";
//     $(".sqxx").html(sqxx); //申请信息          
// }

//table搜索
function search(obj){         
    var value=$(obj).val();
    if(value==""){
        $("tr").show();
    }
    else{
        $("td[name=search]").each(function(){
            if(this.innerHTML.indexOf(value)>=0){
                $(this).parent().show();
            }                       
            else{
                $(this).parent().hide();
            }
                
        })
    }

}