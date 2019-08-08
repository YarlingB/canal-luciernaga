(function($){
    $(document).ready(function() {
        $('#change_id_tipo').hide();

        var selectField = $('#id_tipo'),
        verified_url = $('#id_url'),
        verified_inline = $('.inline-group');

        function Verificar(value) {
            if(value.toUpperCase() == 'SERIE' || value.toUpperCase()=='SERIES'){
                verified_url.parent('div').hide();
                verified_inline.show();
            }else{
                verified_url.parent('div').show();
                verified_inline.hide();
            }
        }

        // Verificar(selectField.val());

        selectField.change(function() {
            //Verificar($(this).val());
            var charval = $('#id_tipo option:selected').text();
            Verificar(charval);
        }); 
    
    });

})(jQuery || django.jQuery);
    