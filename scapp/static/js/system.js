// -------------权限管理------------- begin
//功能权限select管理
function change_select(obj,classname){
    if(obj.value == "0"){
        $("." + classname).each(function() {
            $(this).empty();
            $(this).append("<option value='0'>无权限</option>");
        });
    }
    if(obj.value == "1"){
        $("." + classname).each(function() {
            $(this).empty();
            $(this).append("<option value='1'>查询</option><option value='0'>无权限</option>");
        });
    }
    if(obj.value == "2"){
        $("." + classname).each(function() {
            $(this).empty();
            $(this).append("<option value='2'>维护</option><option value='1'>查询</option><option value='0'>无权限</option>");
        });
    }
}

//角色的选取
function addroles(){    
    var select=document.getElementById("selsetroles")
    var roles=document.getElementById("roles")      
    if(select.selectedIndex!=-1){//选取值不为空时执行
        for(j=0;j<roles.options.length;j++){//获取已选职能中的值         
            if(options=roles.options[j].value==select.options[select.selectedIndex].value){//判断已选职能中是否已经包含该值
                    alert("该职能已选择，不能重复选择！！");
                    return
            }           
        }       
        $("<option selected value='"+select.options[select.selectedIndex].value+"'>"+select.options[select.selectedIndex].text+"</option>").appendTo("#roles"); //添加option项
    }
    else
        alert("请先选择职能，然后再添加！！");    
}
//角色的删除
function removeroles(){
    var roles=document.getElementById("roles")
    if(roles.selectedIndex!=-1)
        roles.remove(roles.selectedIndex)   
    else
        alert("请先选择职能，然后再移除！！");
}
// -------------权限管理------------- end

// ------------机构管理------------- begin

// ------------机构管理------------- end

// -------------数据字典------------- begin

// -------------数据字典------------- end