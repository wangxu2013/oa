function switchTab(obj,num){//控制最左边的导航	$(obj).parent().find("li").attr("class","");	$(obj).attr("class","active");	var images=$(obj).parent().find("img")	for(i=0;i<images.length;i++){		images[i].src="/static/img/"+i+".png"		//$("#tab"+i).hide();	}	images[num].src="/static/img/"+num+"_hover.png";	//$("#tab"+num).show();}var s=1;function showORhide(){//显示隐藏侧边栏	if(s==1){						$('.middle').fadeOut("slow");		$('.right').css('left','60px');		$("#show_hide_btn").attr("src","/static/img/nav_show.png");		s=0;	}	else{		$('.middle').fadeIn("slow");		$('.right').css('left','280px');		$("#show_hide_btn").attr("src","/static/img/nav_hide.png");		s=1;	}}function showNav(obj){	if($(obj).attr("src")=="/static/img/nav_item_minus.jpg"){//导航为展开时		$(obj).attr("src","/static/img/nav_item_plus.jpg");		$(obj).parent().parent().find("li").hide();		$(obj).parent().parent().find(".nav_header").show();	}	else{//导航为隐藏时		$(obj).attr("src","/static/img/nav_item_minus.jpg");		$(obj).parent().parent().find("li").show();	}}