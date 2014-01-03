//-----------------------新增贷款申请--------------------------------------
//获取客户信息
function getCustomer(belong_customer_type,belong_customer_value){
	$("#dksq_info").attr("src","/Process/dksq/goto_new_dksq_info/" + belong_customer_type + "/" + belong_customer_value);
	$('#dksq_info').show();
	$('#search').hide();
	Frame();    		
}
//-----------------------现金流分析--------------------------------------
//业务历史&业务展望切换
function xjlfx(obj){
    if(obj.options[obj.selectedIndex].value==0){
        $("#ywls").show();
        $("#ywzw").hide();
    }
    if(obj.options[obj.selectedIndex].value==1){
        $("#ywzw").show();
        $("#ywls").hide();
    }
}
//----------------------贷款申请信息--------------------------
//表格添加行
function addTd(table,frameid){
	
    if(table=="haveCredit"){//是否申请过贷款
        $("#"+table).append("<tr class='add'>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                                "<td><input type='text' id='' class='tbInput'/></td>" + 
                            "</tr>");      
    }
    if(table=="sfwtrdb"){//是否为他人担保
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='bank' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>	"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='guarantor' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>	"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='guarantee_amount' onkeyup='setJe(this);' maxlength='11' /><br/>"+
										"<span class='je'>￥</span>"+
										"<span class='errorInfo'></span>"+				
									"</span>"+
								"</td>"	+
                               /*  "<td><input type='text' name='bank' /></td>"+
                                "<td><input type='text' name='guarantor'/></td>"+
                                "<td><input type='text' name='guarantee_amount'/></td>"+ */
                            "</tr>");      
    }
    if(table=="ywdyw"){//有无抵押物
        $("#"+table).append("<tr class='add'>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='obj_name' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>	" +		
								"<td>" +
									"<span>	" +
										"<input type='text' name='owner_address' onchange='spryMaxLength(this,128)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于128</span>" +
									"</span>" +
								"</td>	" +			
								"<td>" +
									"<span>	" +
										"<input type='text' name='description' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>	" +
								"<td>" +
									"<input type='text' name='registration_number' onkeyup='' maxlength='11' class='tbInput'/><br/>" +
									"<span>&nbsp;</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='appraisal' onkeyup='setJe(this);' maxlength='11' class='tbInput'/><br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='mortgage' onkeyup='setJe(this);' maxlength='11' class='tbInput'/><br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' name='obj_name' class='tbInput'/></td>" + 
                                "<td><input type='text' name='owner_address'  class='tbInput'/></td>" + 
                                "<td><input type='text' name='description'  class='tbInput'/></td>" + 
                                "<td><input type='text' name='registration_number'  class='tbInput'/></td>" +
                                "<td><input type='text' name='appraisal'  class='tbInput'/></td>" +
                                "<td><input type='text' name='mortgage'  class='tbInput'/></td>" + */
                            "</tr>");    
    }
    if(table=="dbInformation"){//担保信息
        $("#"+table).append("<tr class='add'>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='name_db' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='address_db' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>		" +					
								"<td>" +
									"<span>	" +
										"<input type='text' name='id_number_db' onchange='checkIdcard(this)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>证件号码有误</span>" +
									"</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='workunit_db' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='phone_db' class='tbInput' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' onblur='getLength(this)'/><br/>&nbsp;" +
										"<span class='errorInfo'>电话号码有误</span>" +
									"</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='relationship_db' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' name='name_db' class='tbInput'/></td>" +
                                "<td><input type='text' name='address_db' class='tbInput'/></td>" +
                                "<td><input type='text' name='id_number_db' class='tbInput'/></td>" +
                                "<td><input type='text' name='workunit_db' class='tbInput'/></td>" +
                                "<td><input type='text' name='phone_db' class='tbInput'/></td>" +
                                "<td><input type='text' name='relationship_db' class='tbInput'/></td>" + */
                            "</tr>");
    }	
	if(table=="xdls"){//信贷历史
	
        $("#"+table).append("<tr class='add'>" +
                                "<td>" +
									"<span>	" +
										"<input type='text' name='financing_sources' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='loan_amount' onkeyup='setJe(this);' maxlength='11' class='tbInput'/><br/>" +
										"<span class='je'>￥</span>	" +
										"<span class='errorInfo'></span>" +					
									"</span>" +
								"</td>" +	
								"<td>" +
									"<select name='deadline' style='width:60px'>"+
										"<option value='1'>1</option>"+
										"<option value='2'>2</option>"+
										"<option value='3'>3</option>"+
										"<option value='4'>4</option>"+
										"<option value='5'>5</option>"+
										"<option value='6'>6</option>"+
										"<option value='7'>7</option>"+
										"<option value='8'>8</option>"+
										"<option value='9'>9</option>"+
										"<option value='10'>10</option>"+
										"<option value='11'>11</option>"+
										"<option value='12'>12</option>"+
										"<option value='13'>13</option>"+
										"<option value='14'>14</option>"+
										"<option value='15'>15</option>"+
										"<option value='16'>16</option>"+
										"<option value='17'>17</option>"+
										"<option value='18'>18</option>"+
										"<option value='19'>19</option>"+
										"<option value='20'>20</option>"+
										"<option value='21'>21</option>"+
										"<option value='22'>22</option>"+
										"<option value='23'>23</option>"+
										"<option value='24'>24</option>"+
									"</select><br/>&nbsp;"+
									/* "<input type='text' name='deadline' onkeyup='' maxlength='5' class='tbInput'/><br/>" +
									"<span>&nbsp;</span>" + */
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='use' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>" +
										"<input type='text' name='release_date' class='tbInput datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>" +
										"<span>&nbsp;</span>" +								
									"</span>" +					
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='overage' onkeyup='setJe(this);' maxlength='11' class='tbInput'/><br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>	" +
								"<td>" +
									"<span >	" +
										"<input type='text' name='guarantee' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span >	" +
										"<input type='text' name='late_information' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>		" +
                                // "<td><input type='text' name='financing_sources' class='tbInput'/></td>" +
                                // "<td><input type='text' name='loan_amount' class='tbInput'/></td>" +
                                // "<td><input type='text' name='deadline' class='tbInput'/></td>" +
                                // "<td><input type='text' name='use' class='tbInput'/></td>" +
                                // "<td><input type='text' name='release_date' class='tbInput datepicker'/></td>" +
                                // "<td><input type='text' name='overage' class='tbInput'/></td>" +
                                // "<td><input type='text' name='guarantee' class='tbInput'/></td>" +
                                // "<td><input type='text' name='late_information' class='tbInput'/></td>" +
                            "</tr>");
        // $("input[name='release_date']").live("focus", function () {
        //     $(this).datepicker({ dateFormat: "yy-mm-dd", changeMonth: true, changeYear: true });
        // });
        datepicker();
    }
	if(table=="gtjkr"){//共同借款人
        $("#"+table).append("<tr class='add'>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='name' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='relationship' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>		" +					
								"<td>" +
									"<span>	" +
										"<input type='text' name='id_number' onchange='checkIdcard(this)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>证件号码有误</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='phone' class='tbInput' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' onblur='getLength(this)'/><br/>&nbsp;" +
										"<span class='errorInfo'>电话号码有误</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='main_business' onchange='spryMaxLength(this,128)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于128</span>" +
									"</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='address' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='major_assets' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='monthly_income' onkeyup='setJe(this);' maxlength='11' class='tbInput'/><br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>		" +				
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' name='name' class='tbInput'/></td>" +
                                "<td><input type='text' name='relationship' class='tbInput'/></td>" +
                                "<td><input type='text' name='id_number' class='tbInput'/></td>" +
                                "<td><input type='text' name='phone' class='tbInput'/></td>" +
                                "<td><input type='text' name='main_business' class='tbInput'/></td>" +
                                "<td><input type='text' name='address' class='tbInput'/></td>" +
                                "<td><input type='text' name='major_assets' class='tbInput'/></td>" +
                                "<td><input type='text' name='monthly_income' class='tbInput'/></td>" + */
                            "</tr>");
    }
    if(table=="dbr"){//担保人
        $("#"+table).append("<tr class='add'>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='name_db' value='' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='address_db' value='' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>" +							
								"<td>" +
									"<span>	" +
										"<input type='text' name='id_number_db' value='' onchange='checkIdcard(this)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>证件号码有误</span>" +
									"</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='workunit_db' value='' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<input type='text' name='phone_db' value='' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' class='tbInput'/><br/>" +
									"<span>&nbsp;</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='relationship_db' value='' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>" +
								"<!--add By WX-->" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='major_assets' value='' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='monthly_income' value='' onkeyup='setJe(this);' maxlength='11' class='tbInput' onclick='setJe(this);'/><br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                // "<td><select id=''  style='width:80px;'></select></td>" +
                                // "<td><span id=''></span></td>" +
                                // "<td><span id=''></span></td>" +
                                // "<td><span id=''></span></td>" +
                                // "<td><input type='text' id='' style='width:100px;'/></td>" +
                                // "<td><input type='text' id='' style='width:130px;'/></td>" +
                                // "<td><input type='text' id='' style='width:90px;'/></td>" +
                                // "<td><input type='text' id='' style='width:90px;'/></td>" +
                            "</tr>");
    }
    if(table=="jydyw"){//建议抵押物
        $("#"+table).append("<tr class='add'>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='obj_name' value='' onchange='spryMaxLength(this,32)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于32</span>" +
									"</span>" +
								"</td>		" +	
								"<td>" +
									"<span>	" +
										"<input type='text' name='owner_address' value='' onchange='spryMaxLength(this,128)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于128</span>" +
									"</span>" +
								"</td>		" +		
								"<td>" +
									"<span>	" +
										"<input type='text' name='description' value='' onchange='spryMaxLength(this,256)' class='tbInput'/><br/>" +
										"<span>&nbsp;</span>" +
										"<span class='errorInfo'>字符数不得大于256</span>" +
									"</span>" +
								"</td>	" +
								"<td>" +
									"<input type='text' name='registration_number' value='' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' class='tbInput'/><br/>" +
									"<span>&nbsp;</span>" +
								"</td>	" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='appraisal' value='' onkeyup='setJe(this);' maxlength='11' class='tbInput' onclick='setJe(this)'/><br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>		" +				
									"</span>" +
								"</td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='mortgage' value='' onkeyup='setJe(this);' maxlength='11' class='tbInput' onclick='setJe(this)'/><br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>		" +		
								"<td><input type='checkbox' id=''/></td>	" +
                                // "<td><input type='text' id='' class='tbInput'/></td>" +
                                // "<td><input type='text' id=''  class='tbInput'/></td>" +
                                // "<td><input type='text' id=''  class='tbInput'/></td>" +
                                // "<td><input type='text' id=''  class='tbInput'/></td>" +
                                // "<td><input type='text' id=''  class='tbInput'/></td>" +
                                // "<td><input type='text' id=''  class='tbInput'/></td>" +
                                // "<td><input type='checkbox' id=''/></td>" +
                            "</tr>");
    }
	//----------------------贷前调查——资产负债表--------------------------
    if(table=="yfzk"){//现金及银行存款&应付账款
        $("#"+table).append("<tr class='add'>" +
								"<td><input type='text' name='name_0'/>"+
								"<input type='hidden' name='type_0' value='0'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_0' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
								"<td><input type='text' name='name_1'/>"+
								"<input type='hidden' name='type_1' value='1'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_1' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" + */
                            "</tr>");
    }
    if(table=="yszk"){//应收账款&预收账款
        $("#"+table).append("<tr class='add'>" +
								"<td><input type='text' name='name_2'/>"+
								"<input type='hidden' name='type_2' value='2'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_2' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
								"<td><input type='text' name='name_3'/>"+
								"<input type='hidden' name='type_3' value='3'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_3' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" + */
                            "</tr>");		
    }
    if(table=="yfkx"){//预付款项&短期借款
        $("#"+table).append("<tr class='add'>" +
								"<td><input type='text' name='name_4'/>"+
								"<input type='hidden' name='type_4' value='4'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_4' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
								"<td><input type='text' name='name_5'/>"+
								"<input type='hidden' name='type_5' value='5'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_5' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" + */
                            "</tr>");	
    }
    if(table=="ch"){//存货&社会集资
        $("#"+table).append("<tr class='add'>" +
								"<td><input type='text' name='name_6'/>"+
								"<input type='hidden' name='type_6' value='6'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_6' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
								"<td><input type='text' name='name_7'/>"+
								"<input type='hidden' name='type_7' value='7'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_7' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" + */
                            "</tr>");	
    }
    if(table=="gdzc"){//固定资产&长期借款
        $("#"+table).append("<tr class='add'>" +
								"<td><input type='text' name='name_10'/>"+
								"<input type='hidden' name='type_10' value='10'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_10' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
								"<td><input type='text' name='name_11'/>"+
								"<input type='hidden' name='type_11' value='11'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_11' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" + */
                            "</tr>");	
    }
    if(table=="qt"){//其他经营资产&其他
        $("#"+table).append("<tr class='add'>" +
								"<td><input type='text' name='name_12'/>"+
								"<input type='hidden' name='type_12' value='12'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_12' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
								"<td><input type='text' name='name_13'/>"+
								"<input type='hidden' name='type_13' value='13'></td>" +
								"<td>" +
									"<span>	" +
										"<input type='text' name='value_13' onkeyup='setJe(this);' maxlength='11' onclick='setJe(this)'/>" +
										"<br/>" +
										"<span class='je'>￥</span>" +
										"<span class='errorInfo'></span>	" +					
									"</span>" +
								"</td>" +
                                /* "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" +
                                "<td><input type='text' id=''/></td>" + */
                            "</tr>");	
    } 
//----------------------贷前调查——益损表--------------------------	
    if(table=="sr"){//收入
        $("#"+table).append("<tr class='add'>"+
								"<td style='width:166px;'>"+
									"<span>	"+
										"<input type='text' name='items_name_1' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_1_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_1_1','month_1_2');totalSum(2);totalAve(2);cut('month_1_2','month_1_4','month_1_5');totalSum(5);totalAve(5);cut4('month_1_2','month_1_4','month_1_23','month_1_24','month_1_25');other(1);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_2_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_2_1','month_2_2');totalSum(2);totalAve(2);cut('month_2_2','month_2_4','month_2_5');totalSum(5);totalAve(5);cut4('month_2_2','month_2_4','month_2_23','month_2_24','month_2_25');other(2);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_3_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_3_1','month_3_2');totalSum(2);totalAve(2);cut('month_3_2','month_3_4','month_3_5');totalSum(5);totalAve(5);cut4('month_3_2','month_3_4','month_3_23','month_3_24','month_3_25');other(3);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_4_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_4_1','month_4_2');totalSum(2);totalAve(2);cut('month_4_2','month_4_4','month_4_5');totalSum(5);totalAve(5);cut4('month_4_2','month_4_4','month_4_23','month_4_24','month_4_25');other(4);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_5_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_5_1','month_5_2');totalSum(2);totalAve(2);cut('month_5_2','month_5_4','month_5_5');totalSum(5);totalAve(5);cut4('month_5_2','month_5_4','month_5_23','month_5_24','month_5_25');other(5);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_6_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_6_1','month_6_2');totalSum(2);totalAve(2);cut('month_6_2','month_6_4','month_6_5');totalSum(5);totalAve(5);cut4('month_6_2','month_6_4','month_6_23','month_6_24','month_6_25');other(6);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_7_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_7_1','month_7_2');totalSum(2);totalAve(2);cut('month_7_2','month_7_4','month_7_5');totalSum(5);totalAve(5);cut4('month_7_2','month_7_4','month_7_23','month_7_24','month_7_25');other(7);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_8_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_8_1','month_8_2');totalSum(2);totalAve(2);cut('month_8_2','month_8_4','month_8_5');totalSum(5);totalAve(5);cut4('month_8_2','month_8_4','month_8_23','month_8_24','month_8_25');other(8);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_9_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_9_1','month_9_2');totalSum(2);totalAve(2);cut('month_9_2','month_9_4','month_9_5');totalSum(5);totalAve(5);cut4('month_9_2','month_9_4','month_9_23','month_9_24','month_9_25');other(9);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_10_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_10_1','month_10_2');totalSum(2);totalAve(2);cut('month_10_2','month_10_4','month_10_5');totalSum(5);totalAve(5);cut4('month_10_2','month_10_4','month_10_23','month_10_24','month_10_25');other(10);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_11_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_11_1','month_11_2');totalSum(2);totalAve(2);cut('month_11_2','month_11_4','month_11_5');totalSum(5);totalAve(5);cut4('month_11_2','month_11_4','month_11_23','month_11_24','month_11_25');other(11);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_12_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,1);average(this,1);total('month_12_1','month_12_2');totalSum(2);totalAve(2);cut('month_12_2','month_12_4','month_12_5');totalSum(5);totalAve(5);cut4('month_12_2','month_12_4','month_12_23','month_12_24','month_12_25');other(12);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+			
								"<td>"+
									"<input type='text' name='total_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' value='0' maxlength='11' readonly/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='pre_month_1' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' value='0' maxlength='11' readonly/>"+
								"</td>"+	
								/* "<td style='width:166px;'>"+
									"<span>	"+
										"<input type='text' name='' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' onkeyup='setJe(this);' onclick='setJe(this)' maxlength='11'/><br/>"+
										"<span  class='je'>￥</span>"+
										"<span class='errorInfo'></span>		"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' onkeyup='setJe(this);' onclick='setJe(this)' maxlength='11'/><br/>"+
										"<span  class='je'>￥</span>"+
										"<span class='errorInfo'></span>	"+							
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' onkeyup='setJe(this);' onclick='setJe(this)' maxlength='11'/><br/>"+
										"<span  class='je'>￥</span>"+
										"<span class='errorInfo'></span>"+								
									"</span>"+
								"</td>	"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' onkeyup='setJe(this);' onclick='setJe(this)' maxlength='11'/><br/>"+
										"<span  class='je'>￥</span>"+
										"<span class='errorInfo'></span>"+								
									"</span>"+
								"</td>		"+ */
							"</tr>");
    }
    if(table=="kbcb"){//可变成本
       $("#"+table).append("<tr class='add'>"+
								"<td style='width:166px;'>"+
									"<span>	"+
										"<input type='text' name='items_name_3' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_1_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_1_3','month_1_4');totalSum(4);totalAve(4);cut('month_1_2','month_1_4','month_1_5');totalSum(5);totalAve(5);cut4('month_1_2','month_1_4','month_1_23','month_1_24','month_1_25');other(1);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_2_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_2_3','month_2_4');totalSum(4);totalAve(4);cut('month_2_2','month_2_4','month_2_5');totalSum(5);totalAve(5);cut4('month_2_2','month_2_4','month_2_23','month_2_24','month_2_25');other(2);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_3_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_3_3','month_3_4');totalSum(4);totalAve(4);cut('month_3_2','month_3_4','month_3_5');totalSum(5);totalAve(5);cut4('month_3_2','month_3_4','month_3_23','month_3_24','month_3_25');other(3);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_4_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_4_3','month_4_4');totalSum(4);totalAve(4);cut('month_4_2','month_4_4','month_4_5');totalSum(5);totalAve(5);cut4('month_4_2','month_4_4','month_4_23','month_4_24','month_4_25');other(4);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_5_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_5_3','month_5_4');totalSum(4);totalAve(4);cut('month_5_2','month_5_4','month_5_5');totalSum(5);totalAve(5);cut4('month_5_2','month_5_4','month_5_23','month_5_24','month_5_25');other(5);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_6_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_6_3','month_6_4');totalSum(4);totalAve(4);cut('month_6_2','month_6_4','month_6_5');totalSum(5);totalAve(5);cut4('month_6_2','month_6_4','month_6_23','month_6_24','month_6_25');other(6);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_7_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_7_3','month_7_4');totalSum(4);totalAve(4);cut('month_7_2','month_7_4','month_7_5');totalSum(5);totalAve(5);cut4('month_7_2','month_7_4','month_7_23','month_7_24','month_7_25');other(7);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_8_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_8_3','month_8_4');totalSum(4);totalAve(4);cut('month_8_2','month_8_4','month_8_5');totalSum(5);totalAve(5);cut4('month_8_2','month_8_4','month_8_23','month_8_24','month_8_25');other(8);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_9_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_9_3','month_9_4');totalSum(4);totalAve(4);cut('month_9_2','month_9_4','month_9_5');totalSum(5);totalAve(5);cut4('month_9_2','month_9_4','month_9_23','month_9_24','month_9_25');other(9);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_10_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_10_3','month_10_4');totalSum(4);totalAve(4);cut('month_10_2','month_10_4','month_10_5');totalSum(5);totalAve(5);cut4('month_10_2','month_10_4','month_10_23','month_10_24','month_10_25');other(10);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_11_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_11_3','month_11_4');totalSum(4);totalAve(4);cut('month_11_2','month_11_4','month_11_5');totalSum(5);totalAve(5);cut4('month_11_2','month_11_4','month_11_23','month_11_24','month_11_25');other(11);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_12_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,3);average(this,3);total('month_12_3','month_12_4');totalSum(4);totalAve(4);cut('month_12_2','month_12_4','month_12_5');totalSum(5);totalAve(5);cut4('month_12_2','month_12_4','month_12_23','month_12_24','month_12_25');other(12);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='total_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' value='0' readonly/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='pre_month_3' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' value='0' readonly/>"+
								"</td>"+	
							"</tr>");
    }
    if(table=="qtfy"){//其他费用
       $("#"+table).append("<tr class='add'>"+
								"<td style='width:166px;'>"+
									"<span>	"+
										"<input type='text' name='items_name_21' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_1_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_1_');totalSum(23);totalAve(23);cut4('month_1_2','month_1_4','month_1_23','month_1_24','month_1_25');other(1);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_2_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_2_');totalSum(23);totalAve(23);cut4('month_2_2','month_2_4','month_2_23','month_2_24','month_2_25');other(2);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_3_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_3_');totalSum(23);totalAve(23);cut4('month_3_2','month_3_4','month_3_23','month_3_24','month_3_25');other(3);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_4_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_4_');totalSum(23);totalAve(23);cut4('month_4_2','month_4_4','month_4_23','month_4_24','month_4_25');other(4);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_5_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_5_');totalSum(23);totalAve(23);cut4('month_5_2','month_5_4','month_5_23','month_5_24','month_5_25');other(5);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_6_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_6_');totalSum(23);totalAve(23);cut4('month_6_2','month_6_4','month_6_23','month_6_24','month_6_25');other(6);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_7_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_7_');totalSum(23);totalAve(23);cut4('month_7_2','month_7_4','month_7_23','month_7_24','month_7_25');other(7);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_8_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_8_');totalSum(23);totalAve(23);cut4('month_8_2','month_8_4','month_8_23','month_8_24','month_8_25');other(8);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_9_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_9_');totalSum(23);totalAve(23);cut4('month_9_2','month_9_4','month_9_23','month_9_24','month_9_25');other(9);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_10_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_10_');totalSum(23);totalAve(23);cut4('month_10_2','month_10_4','month_10_23','month_10_24','month_10_25');other(10);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_11_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_11_');totalSum(23);totalAve(23);cut4('month_11_2','month_11_4','month_11_23','month_11_24','month_11_25');other(11);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_12_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,21);average(this,21);total3('month_12_');totalSum(23);totalAve(23);cut4('month_12_2','month_12_4','month_12_23','month_12_24','month_12_25');other(12);totalSum(25);totalAve(25);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='total_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' value='0' maxlength='11' readonly/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='pre_month_21' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' value='0' maxlength='11' readonly/>"+
								"</td>"+	
							"</tr>");
    }
    if(table=="qtzc"){//其他支出
       $("#"+table).append("<tr class='add'>"+
								"<td style='width:166px;'>"+
									"<span>	"+
										"<input type='text' name='items_name_28' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_1_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(1);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_2_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(2);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_3_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(3);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_4_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(4);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_5_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(5);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_6_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(6);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_7_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(7);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_8_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(8);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_9_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(9);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_10_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(10);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_11_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(11);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_12_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,28);average(this,28);other(12);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='total_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' value='0' readonly/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='pre_month_28' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' value='0' readonly/>"+
								"</td>"+	
							"</tr>");
    }
    if(table=="qtsr"){//其他收入
       $("#"+table).append("<tr class='add'>"+
								"<td style='width:166px;'>"+
									"<span>	"+
										"<input type='text' name='items_name_29' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_1_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(1);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_2_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(2);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_3_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(3);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_4_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(4);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_5_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(5);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_6_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(6);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_7_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(7);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_8_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(8);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_9_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(9);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_10_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(10);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_11_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(11);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='month_12_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' onchange=\"sum(this,29);average(this,29);other(12);totalSum(30);totalAve(30);\"/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='total_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' value='0' readonly/>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='pre_month_29' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='11' value='0' readonly/>"+
								"</td>"+	
							"</tr>");
    }
    if(table=="zyywlrfx"){//主营业务利润分析
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' value='' style='width:100px;' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' onkeyup='setJe(this);' onclick='setJe(this)' style='width:100px;' maxlength='11'/><br/>"+
										"<span  class='je'>￥</span>"+
										"<span class='errorInfo'></span>		"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' onkeyup='setJe(this);' onclick='setJe(this)' style='width:100px;' maxlength='11'/><br/>"+
										"<span  class='je'>￥</span>"+
										"<span class='errorInfo'></span>"+								
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='' onkeyup='setJe(this);' onclick='setJe(this)' style='width:100px;' maxlength='11'/><br/>"+
										"<span  class='je'>￥</span>"+
										"<span class='errorInfo'></span>		"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' style='width:40px' name='' onKeyUp='value=value.replace(/\D/g,'')' maxlength='4' onchange='check(this,0,100)'/>%<br/>"+
										"<span class='errorInfo'>请输入0-100的数</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' style='width:40px' name='' onKeyUp='value=value.replace(/\D/g,'')' maxlength='4' onchange='check(this,0,100)'/>%<br/>"+
										"<span class='errorInfo'>请输入0-100的数</span>"+
									"</span>"+
								"</td>	"+
							"</tr>");
    }
//----------------------基本情况--------------------------
    if(table=="zxjl"){//征信记录
        $("#"+table).append("<tr class='add'><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td></tr>");
    }
    if(table=="wtrdbqk"){//为他人担保情况
        $("#"+table).append("<tr class='add'><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td></tr>");
    }
 //----------------------资产负债表--------------------------   
    if(table=="ck"){//存款
        $("#"+table).append("<tr class='add'>"+
								"<td>"+												
									"<span>"+
										"<input type='text' name='bank' onchange='spryMaxLength(this,64)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于64</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='account_type' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='account_no' onkeyup='value=value.replace(/[^0-9a-zA-Z]/g,&apos;&apos;)' onchange='spryMaxLength(this,22)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于22</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='account_balance' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+	
									"</span>"+
								"</td>"+
							"</tr>");
    }
    if(table=="yhcshp"){//未到期的银行程税汇票
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='bank' onchange='spryMaxLength(this,64)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于64</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='account_expiry_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='account_balance' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>	"+
								"</td>		"+
							"</tr>");
		datepicker();
    }
    if(table=="Yszk"){//应收账款
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='customer_name' onchange='spryMaxLength(this,64)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于64</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' style='width:40px' name='proportion' onKeyUp='value=value.replace(/[^0-9\.]/g,&apos;&apos;)' onchange='check(this,0,100)' maxlength='4'/>%<br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>请输入0-100的数</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+	
								"</td>"+
							"</tr>");
    }
    if(table=="Yfzk1"){//预付账款
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='customer_name' onchange='spryMaxLength(this,64)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于64</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' style='width:40px' name='proportion' onKeyUp='value=value.replace(/[^0-9\.]/g,&apos;&apos;)' onchange='check(this,0,100)' maxlength='4'/>%<br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>请输入0-100的数</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+	
								"</td>"+
							"</tr>");
    }
    if(table=="Ch"){//存货(元)
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='stock_type' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='stock_evaluate' onchange='spryMaxLength(this,64)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于64</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='stock_mobility' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' style='width:40px' name='proportion' onKeyUp='value=value.replace(/[^0-9\.]/g,&apos;&apos;)' onchange='check(this,0,100)' maxlength='4'/>%<br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>请输入0-100的数</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>		"+					
									"</span>"+
								"</td>		"+	
							"</tr>");
    }  
    if(table=="fdc"){//固定资产-房地产
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='assets_name' onchange='spryMaxLength(this,128)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于128</span>"+
									"</span>"+
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='assets_ah' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='assets_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='price' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>	"+
							"</tr>");
		datepicker();
    }  
    if(table=="sb"){//固定资产-设备
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='assets_name' onchange='spryMaxLength(this,128)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于128</span>"+
									"</span>"+
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='assets_ah' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='assets_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='price' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>	"+
							"</tr>");
		datepicker();
    } 
    if(table=="cl"){//固定资产-车辆
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='assets_name' onchange='spryMaxLength(this,128)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于128</span>"+
									"</span>"+
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='assets_ah' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='assets_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='price' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>	"+
							"</tr>");
		datepicker();
    }   
    if(table=="Qtjyzc"){//其它经营资产(元)
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='project' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>	"+		
							"</tr>");
    } 
    if(table=="bwzc"){//其它非经营资产或表外资产
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='project' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='project_owner' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+					
									"</span>"+
								"</td>	"+	
							"</tr>");
    } 
    if(table=="yfgyszk"){//应付供货商账款
        $("#"+table).append("<tr class='add'>"+	
								"<td>"+
									"<span>"+
										"<input type='text' name='customer_name' onchange='spryMaxLength(this,64)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于64</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>	"+
							"</tr>");
    } 
    if(table=="qtyfzk"){//其他应付帐款
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='customer_name' onchange='spryMaxLength(this,64)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于64</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>	"+	
							"</tr>");
    } 
    if(table=="yszky"){//预收账款(元)
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='source' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='occur_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='describe' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>"+							
									"</span>"+
								"</td>	"+
							"</tr>");
		datepicker();
    } 
    if(table=="dqyhjk"){//短期银行借款
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='loan_org' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='loan_amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='occur_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>	"+
								"<td>"+
									"<select name='loan_deadline' style='width:60px'>"+
										"<option value='1'>1</option>"+
										"<option value='2'>2</option>"+
										"<option value='3'>3</option>"+
										"<option value='4'>4</option>"+
										"<option value='5'>5</option>"+
										"<option value='6'>6</option>"+
										"<option value='7'>7</option>"+
										"<option value='8'>8</option>"+
										"<option value='9'>9</option>"+
										"<option value='10'>10</option>"+
										"<option value='11'>11</option>"+
										"<option value='12'>12</option>"+
										"<option value='13'>13</option>"+
										"<option value='14'>14</option>"+
										"<option value='15'>15</option>"+
										"<option value='16'>16</option>"+
										"<option value='17'>17</option>"+
										"<option value='18'>18</option>"+
										"<option value='19'>19</option>"+
										"<option value='20'>20</option>"+
										"<option value='21'>21</option>"+
										"<option value='22'>22</option>"+
										"<option value='23'>23</option>"+
										"<option value='24'>24</option>"+
									"</select><br/>&nbsp;"+
									/* "<input type='text' name='loan_deadline' onKeyUp='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='4'/><br/>"+
									"<span>&nbsp;</span>"+ */
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='guarantee' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>	"+	
								"<td>"+
									"<span>	"+
										"<input type='text' name='banlance' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>	"+	
							"</tr>");
		datepicker();
    } 
    if(table=="dqshjz"){//短期社会集资
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='loan_org' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='loan_amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='occur_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>	"+
								"<td>"+
									/* "<input type='text' name='loan_deadline' onKeyUp='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='4'/><br/>"+
									"<span>&nbsp;</span>"+ */
									"<select name='loan_deadline' style='width:60px'>"+
										"<option value='1'>1</option>"+
										"<option value='2'>2</option>"+
										"<option value='3'>3</option>"+
										"<option value='4'>4</option>"+
										"<option value='5'>5</option>"+
										"<option value='6'>6</option>"+
										"<option value='7'>7</option>"+
										"<option value='8'>8</option>"+
										"<option value='9'>9</option>"+
										"<option value='10'>10</option>"+
										"<option value='11'>11</option>"+
										"<option value='12'>12</option>"+
										"<option value='13'>13</option>"+
										"<option value='14'>14</option>"+
										"<option value='15'>15</option>"+
										"<option value='16'>16</option>"+
										"<option value='17'>17</option>"+
										"<option value='18'>18</option>"+
										"<option value='19'>19</option>"+
										"<option value='20'>20</option>"+
										"<option value='21'>21</option>"+
										"<option value='22'>22</option>"+
										"<option value='23'>23</option>"+
										"<option value='24'>24</option>"+
									"</select><br/>&nbsp;"+
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='guarantee' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>	"+	
								"<td>"+
									"<span>	"+
										"<input type='text' name='banlance' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>	"+	
							"</tr>");
		datepicker();
    } 
    if(table=="cqyhjk"){//长期银行借款
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='loan_org' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='loan_amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='occur_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>	"+
								"<td>"+
									"<select name='loan_deadline' style='width:60px'>"+
										"<option value='1'>1</option>"+
										"<option value='2'>2</option>"+
										"<option value='3'>3</option>"+
										"<option value='4'>4</option>"+
										"<option value='5'>5</option>"+
										"<option value='6'>6</option>"+
										"<option value='7'>7</option>"+
										"<option value='8'>8</option>"+
										"<option value='9'>9</option>"+
										"<option value='10'>10</option>"+
										"<option value='11'>11</option>"+
										"<option value='12'>12</option>"+
										"<option value='13'>13</option>"+
										"<option value='14'>14</option>"+
										"<option value='15'>15</option>"+
										"<option value='16'>16</option>"+
										"<option value='17'>17</option>"+
										"<option value='18'>18</option>"+
										"<option value='19'>19</option>"+
										"<option value='20'>20</option>"+
										"<option value='21'>21</option>"+
										"<option value='22'>22</option>"+
										"<option value='23'>23</option>"+
										"<option value='24'>24</option>"+
									"</select><br/>&nbsp;"+
									/* "<input type='text' name='loan_deadline' onKeyUp='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='4'/><br/>"+
									"<span>&nbsp;</span>"+ */
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='guarantee' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>	"+	
								"<td>"+
									"<span>	"+
										"<input type='text' name='banlance' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>	"+	
							"</tr>");
		datepicker();
    }
    if(table=="cqshjz"){//长期社会集资
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='loan_org' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='loan_amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='occur_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>	"+
								"<td>"+
									/* "<input type='text' name='loan_deadline' onKeyUp='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='4'/><br/>"+
									"<span>&nbsp;</span>"+ */
									"<select name='loan_deadline' style='width:60px'>"+
										"<option value='1'>1</option>"+
										"<option value='2'>2</option>"+
										"<option value='3'>3</option>"+
										"<option value='4'>4</option>"+
										"<option value='5'>5</option>"+
										"<option value='6'>6</option>"+
										"<option value='7'>7</option>"+
										"<option value='8'>8</option>"+
										"<option value='9'>9</option>"+
										"<option value='10'>10</option>"+
										"<option value='11'>11</option>"+
										"<option value='12'>12</option>"+
										"<option value='13'>13</option>"+
										"<option value='14'>14</option>"+
										"<option value='15'>15</option>"+
										"<option value='16'>16</option>"+
										"<option value='17'>17</option>"+
										"<option value='18'>18</option>"+
										"<option value='19'>19</option>"+
										"<option value='20'>20</option>"+
										"<option value='21'>21</option>"+
										"<option value='22'>22</option>"+
										"<option value='23'>23</option>"+
										"<option value='24'>24</option>"+
									"</select><br/>&nbsp;"+
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='guarantee' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>	"+	
								"<td>"+
									"<span>	"+
										"<input type='text' name='banlance' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>	"+	
							"</tr>");
		datepicker();
    }
    if(table=="qtbwfz"){//其他表外负债
        $("#"+table).append("<tr class='add'>"+
								"<td>"+
									"<span>"+
										"<input type='text' name='loan_org' onchange='spryMaxLength(this,32)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于32</span>"+
									"</span>"+
								"</td>"+
								"<td>"+
									"<span>	"+
										"<input type='text' name='loan_amount' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>"+
								"<td>"+
									"<input type='text' name='occur_date' class='datepicker' data-date-format='yyyy-mm-dd' readonly/><br/>"+
									"<span>&nbsp;</span>"+
								"</td>	"+
								"<td>"+
									/* "<input type='text' name='loan_deadline' onKeyUp='value=value.replace(/[^0-9]/g,&apos;&apos;)' maxlength='4'/><br/>"+
									"<span>&nbsp;</span>"+ */
									"<select name='loan_deadline' style='width:60px'>"+
										"<option value='1'>1</option>"+
										"<option value='2'>2</option>"+
										"<option value='3'>3</option>"+
										"<option value='4'>4</option>"+
										"<option value='5'>5</option>"+
										"<option value='6'>6</option>"+
										"<option value='7'>7</option>"+
										"<option value='8'>8</option>"+
										"<option value='9'>9</option>"+
										"<option value='10'>10</option>"+
										"<option value='11'>11</option>"+
										"<option value='12'>12</option>"+
										"<option value='13'>13</option>"+
										"<option value='14'>14</option>"+
										"<option value='15'>15</option>"+
										"<option value='16'>16</option>"+
										"<option value='17'>17</option>"+
										"<option value='18'>18</option>"+
										"<option value='19'>19</option>"+
										"<option value='20'>20</option>"+
										"<option value='21'>21</option>"+
										"<option value='22'>22</option>"+
										"<option value='23'>23</option>"+
										"<option value='24'>24</option>"+
									"</select><br/>&nbsp;"+
								"</td>	"+
								"<td>"+
									"<span>"+
										"<input type='text' name='guarantee' onchange='spryMaxLength(this,16)'/><br/>"+
										"<span>&nbsp;</span>"+
										"<span class='errorInfo'>字符数不得大于16</span>"+
									"</span>"+
								"</td>	"+	
								"<td>"+
									"<span>	"+
										"<input type='text' name='banlance' onkeyup='setJe(this)' maxlength='18'/><br/>"+
										"<span class='je'>￥</span>	"+
										"<span class='errorInfo'></span>	"+						
									"</span>"+
								"</td>	"+	
							"</tr>");
		datepicker();
	}
//----------------------损益情况分析--------------------------
    if(table=="jysr"){//经营收入
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="Kbcb"){//可变成本
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="qtcb"){//其他成本
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="qtcb2"){//其他成本2
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="yjmlzh"){//主要经营项目月均毛利组合分析
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
//----------------------现金流分析--------------------------
    if(table=="qtfyx"){//其他费用息
        $("#"+table).append("<tr class='insideTb'>"+
								"<td style='width:225px'><input type='text' name='name_cash_flow_assist_0' value='' style='width:80%'/></td>"+
								"<td><input type='text' name='month_0' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_1' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_2' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_3' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_4' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_5' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_6' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_7' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_8' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_9' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_10' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_11' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_12' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td style='width:80px'><span name='sum'>0</span></td>	"+
							"</tr>");
    } 
    if(table=="qtjk"){//其他借款
        $("#"+table).append("<tr class='insideTb'>"+
								"<td style='width:225px'><input type='text' name='name_cash_flow_assist_1' value='' style='width:80%'/></td>"+
								"<td><input type='text' name='month_0' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_1' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_2' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_3' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_4' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_5' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_6' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_7' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_8' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/ ></td>"+
								"<td><input type='text' name='month_9' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_10' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_11' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_12' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td style='width:80px'><span name='sum'>0</span></td>"+	
							"</tr>");
    } 
    if(table=="chqtjk"){//偿还其他借款
        $("#"+table).append("<tr class='insideTb'>"+
								"<td style='width:225px'><input type='text' name='name_cash_flow_assist_2' value='' style='width:80%'/></td>"+
								"<td><input type='text' name='month_0' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_1' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_2' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_3' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_4' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_5' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_6' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_7' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_8' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_9' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_10' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_11' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_12' value='' onchange='sumqt(this,\"month_\",0)'/></td>"+
								"<td style='width:80px'><span name='sum'>0</span></td>	"+
							"</tr>");
    }
    if(table=="qtjkxjly"){//其他借款现金来源
        $("#"+table).append("<tr class='insideTb'>"+
								"<td style='width:225px'><input type='text' name='name_cash_flow_assist_3' value='' style='width:80%'/></td>"+
								"<td><input type='text' name='month_0' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_1' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_2' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_3' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_4' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_5' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_6' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_7' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_8' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_9' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_10' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_11' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td><input type='text' name='month_12' value='' onchange='sumqt(this,\"month_\",0)' onkeyup='value=value.replace(/[^0-9]/g,&apos;&apos;)'/></td>"+
								"<td style='width:80px'><span name='sum'>0</span></td>	"+
							"</tr>");
    }
//----------------------审贷会决议单--------------------------
	if(table=="jygtdkr"){//建议共同贷款人
        $("#"+table).append("<tr class='insideTb center'>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
							"</tr>");
    }
	if(table=="jydydb"){//建议抵押担保
        $("#"+table).append("<tr class='insideTb center'>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
							"</tr>");
    }
	if(table=="jyzydb"){//建议质押担保
        $("#"+table).append("<tr class='insideTb center'>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
							"</tr>");
    }
	if(table=="jybzdb"){//建议保证担保
        $("#"+table).append("<tr class='insideTb center'>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
								"<td>"+
									"<input type='text' name=''/>"	+
								"</td>"+
							"</tr>");
    }
    doubleIframe(frameid);
}
//表格删除行
function removeTd(table,frameid){   
    //var tr=$("#"+table+' .add')
    //tr.each(function (i){       
       // if(i==tr.length-1)
           // this.remove();
   // });
	if(max==0&&jegs==0&&num==0&&idCard==0){//判断页面中是否有错误，如果未判断直接删除可能导致提交按钮不可用
		var tr= document.getElementById(table).getElementsByTagName("tr");
	    if(tr.length>1){//至少要保留一行
	        document.getElementById(table).deleteRow(tr.length-1);//删除最后一行
	   }
	    doubleIframe(frameid);
	}
    else
    	alert("页面中有错误，请修改后再进行删除操作！")
}

