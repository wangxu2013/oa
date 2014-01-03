var result=new Array()
result['mybx']=new Array()
result['mylx']=new Array()
result['mybj']=new Array()
result['yhqbj']=new Array()
result['yhqbj'][0]=0
//-----------------------等额本息--------------------------------------
function show_calculate(){
    var qs=parseInt($('select[name=loan_period] option:selected').val())//获取输入期数
    var bj=parseFloat($('input[name=loan_amount]').val())//获取输入本金
    var yll=parseFloat($('input[name=annual_interest_rate]').val())/100//获取输入月利率
    var repayment_type=parseInt($('select[name=repayment_type] option:selected').val())
    if (repayment_type=='1')
        result=calculate_debj(bj,yll,qs)
    else
        result=calculate(1,bj,0,yll,qs)
    $('#table_result').html("");    
    for (var n=1;n<=qs;n++){ 
        $ul = $("<tr></tr>");
        $li_qs=$("<td></td>")
        $li_mybx = $("<td></td>");
        $li_mybj = $("<td></td>");
        $li_mylx = $("<td></td>");

		var next_count=parseInt(n)+1
        $ul.append($li_qs.append(n))
        $ul.append($li_mybj.append("<textarea class='tbblur' id='mybj"+n+"' onchange='tqhk("+next_count+","+result['yhqbj'][n-1]+",\"table_result\")'>"+result['mybj'][n]+"</textarea>"))

        $ul.append($li_mylx.append("<span id='mylx"+n+"'>"+result['mylx'][n]+"</span>"))
        $ul.append($li_mybx.append("<span id='mybx"+n+"'>"+result['mybx'][n]+"</span>"))
      
        $('#table_result').append($ul)

    }
    Frame();
    
}

function tqhk(qsqs,yhqbj,table){
    var qs=parseInt($('select[name=loan_period] option:selected').val())
    var bj=parseFloat($('input[name=loan_amount]').val())
    var yll=parseFloat($('input[name=annual_interest_rate]').val())/100
	var qsqs=parseInt(qsqs)
	var syq=qsqs-1
    var syqbj=parseFloat($("#mybj"+syq).val())
    var tr= document.getElementById(table).getElementsByTagName("tr");

    for(tr.length;tr.length>=qsqs;tr.length--){
        document.getElementById(table).deleteRow(tr.length-1);//删除重叠行
    }
    var yhqbj_total=parseFloat(yhqbj)+syqbj

    result=calculate(qsqs,bj,yhqbj_total,yll,qs)
    for (var n=qsqs;n<=qs;n++){
        $ul = $("<tr></tr>");
        $li_qs=$("<td></td>")
        $li_mybx = $("<td></td>");
        $li_mybj = $("<td></td>");
        $li_mylx = $("<td></td>");
        var next_count=parseInt(n)+1
        $ul.append($li_qs.append(n))
        $ul.append($li_mybj.append("<textarea class='tbblur' id='mybj"+n+"' onchange='tqhk("+next_count+","+result['yhqbj'][n-1]+",\"table_result\")'>"+result['mybj'][n]+"</textarea>"))

        $ul.append($li_mylx.append("<span id='mylx"+n+"'>"+result['mylx'][n]+"</span>"))
        $ul.append($li_mybx.append("<span id='mybx"+n+"'>"+result['mybx'][n]+"</span>"))
           
        $('#table_result').append($ul)

    }
    Frame();
}

//-----------------------计算等额本息--------------------------------------
//月还款金额计算公式:每月还款额=[贷款本金×月利率×（1+月利率）^还款月数]÷[（1+月利率）^还款月数—1]
//param:qsqs:起始期数 bj:本金 yhqbj:已还清本金 yll:月利率 zqs:总期数
function calculate(qsqs,bj,yhqbj,yll,zqs){

    qsqs=parseInt(qsqs)
    zqs=parseInt(zqs)
    yll=parseFloat(yll)
    yhqbj=parseFloat(yhqbj)
    bj=parseFloat(bj)

    var syqs=zqs-qsqs+1 //剩余期数
    var bjye=bj-yhqbj //本金余额
    var mybx_value

    var cleared_bj=0 //当前已还清本金
	var yhqbj_total=yhqbj//累计已还清本金
    mybx_value=(bjye*((yll*Math.pow(1+yll,syqs))/(Math.pow(1+yll,syqs)-1))).toFixed(2)//每月本息固定值
	result['yhqbj'][qsqs-1]=yhqbj
	
    
    var count=qsqs
    for (var n=1;n<=syqs;n++){

        result['mybx'][count]=mybx_value
        result['mylx'][count]=((bjye-cleared_bj)*yll).toFixed(2) //每月利息
        result['mybj'][count]=(mybx_value-result['mylx'][count]).toFixed(2)//每月本金
		
		
        cleared_bj+=parseFloat(result['mybj'][count])
		yhqbj_total+=parseFloat(result['mybj'][count])
        result['yhqbj'][count]=yhqbj_total
        count++
    }

    return result
}

//-----------------------计算等额本金--------------------------------------
//param: bj:本金 yhqbj:已还清本金 yll:月利率 zqs:总期数
function calculate_debj(bj,yll,zqs){
    /*月还款金额计算公式:每月还款额=每月本金+每月利息
    当月本金还款=总贷款数÷还款次数
    当月利息=总贷款数×（1－（还款月数-1）÷还款次数）×月利率
    当月月还款额=当月本金还款＋当月利息*/
    var qs=parseInt(zqs)
    var bj=parseFloat(bj)
    var yll=parseFloat(yll)
    var mybj=parseFloat((bj/qs)).toFixed(2)
    var cleared_bj=0 //当前已还清本金
    var yhqbj_total=0//累计已还清本金
    for (var n=1;n<=qs;n++){
        if (n==qs)
            mybj=(bj-result['yhqbj'][qs-1]).toFixed(2)
        result['mybj'][n]=parseFloat(mybj)
        result['mylx'][n]=parseFloat(bj*(1-(n-1)/qs)*yll).toFixed(2)
        result['mybx'][n]=parseFloat(result['mybj'][n])+parseFloat(result['mylx'][n])
        cleared_bj+=parseFloat(result['mybj'][n])
        yhqbj_total+=parseFloat(result['mybj'][n])
        result['yhqbj'][n]=yhqbj_total

    }

    return result
}
