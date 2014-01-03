//-----------------------新增客户--------------------------------------
//客户类型用来显示不同的填写内容
function show_table(value){    
    if(value=="Company"){
        iframe("Information/new_company_customer");  
    }
    if(value=="Individual"){
         iframe("Information/new_individual_customer");
    }
}