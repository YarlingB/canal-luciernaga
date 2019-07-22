(function($){
    $(document).ready(function() {
       
         var selectField = $('#id_tipo'),
        verified_url = $('#id_url'),
        verified_inline = $('.inline-group');

        function Verificar(value) {
            if(value ==1){
                verified_url.parent('div').hide();
                verified_inline.show();
            }else{
                verified_url.parent('div').show();
                verified_inline.hide();
            }
        }

        Verificar(selectField.val());

        selectField.change(function() {
            Verificar($(this).val());
        }); 
    
    });

})(jQuery || django.jQuery);
    