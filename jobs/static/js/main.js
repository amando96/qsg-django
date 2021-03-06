$(document).ready(function(e){  
    $('.search-panel .dropdown-menu').find('a').click(function(e) {
        e.preventDefault();
        var param = $(this).attr("href").replace("#","");
        var concept = $(this).text();
        $('.search-panel span#search_concept').text(concept);
        $('.input-group #search_param').val(param);
        switch(param){
            case 'position':
                $( "#search" ).autocomplete({
                    //serviceUrl: 'autocomplete/positions'
                });
                break;
            case 'company':
                $( "#search" ).autocomplete({
                    //serviceUrl: 'autocomplete/companies'
                });
                break;
            case 'district':
                $( "#search" ).autocomplete({
                    //serviceUrl: 'autocomplete/districts'
                });
                break;
        }
    });
    
   /* $( "#company" ).autocomplete({
        serviceUrl: 'autocomplete/companies'
    });
  
    $( "#position" ).autocomplete({
        serviceUrl: 'autocomplete/positions'
    });*/
	
	function search(){
		$(".spinner").show();
		$("#ajax-results").hide();
		if($("#search_param").val() != ''){
		    by = $("#search_param").val();
		} else {
		    by = 'all';
		}
		$("#ajax-results").load('../makesearch/',
		function(){
		    $("#ajax-results").show();
		    $(".spinner").hide();
		});
	}
	
	$('#search-ajax').click(function(){ $('#search-form').submit(); });
    
 
    $("form").submit(function(e){
        err = false;
        $(".required").each(function(){
            if($(this).val() == ''){
                err = true;
            }
        });
        if(err === true){
            $(".validate-response").html(' <div id="submit-error" class="alert alert-danger" role="alert"><strong>Erro!</strong> Há campos obrigatórios não preenchidos, por favor preencha e volte a submeter.</div>');
            e.preventDefault();
        }
    });

var panels = $('.user-infos');
    var panelsButton = $('.dropdown-user');
    panels.hide();

    //Click dropdown
    panelsButton.click(function() {
        //get data-for attribute
        var dataFor = $(this).attr('data-for');
        var idFor = $(dataFor);

        //current button
        var currentButton = $(this);
        idFor.slideToggle(400, function() {
            //Completed slidetoggle
            if(idFor.is(':visible'))
            {
                currentButton.html('<i class="glyphicon glyphicon-chevron-up text-muted"></i>');
            }
            else
            {
                currentButton.html('<i class="glyphicon glyphicon-chevron-down text-muted"></i>');
            }
        })
    });


    $('[data-toggle="tooltip"]').tooltip();

    $('button').click(function(e) {
        e.preventDefault();
        
    });
});

