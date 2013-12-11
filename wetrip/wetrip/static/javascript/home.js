$(function() {
	$('#elm1').xheditor({
		width : $(window).width() * 0.9,
		height : $(window).height() * 0.7,
		upImgUrl : "upload",
		upImgExt : "jpg,jpeg,gif,png"
	});

	$('input[name="ckb_all"]').click(function() {
		if ($(this).attr('checked')) {
			// all
			$('input[name="ckb_f"]').attr('checked', true);
			$('input[name="ckb_f"]').next().addClass('selected');
		} else {
			// cancel
			$('input[name="ckb_f"]').removeAttr('checked');
			$('input[name="ckb_f"]').next().removeClass('selected');
		}
	})

	$('input[name="sbt_delete"]').click(function() {
		ckbs = 0
		$.each($('input[name="ckb_f"]'), function() {
			if ($(this).attr('checked')) {
				ckbs = ckbs + 1
			}
		})
		if (ckbs == 0) {
			alert('没有选择要删除的项!')
			return false;
		}
	})
	
	$('input[name="ckb_f"]').click(function(){
		if($(this).attr('checked')){
			$(this).next().addClass('selected');
		}else{
			$(this).next().removeClass('selected');
		}
	})
})