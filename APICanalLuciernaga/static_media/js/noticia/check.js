(function($){
    $(document).ready(function() {
       
         var selectField = $('#id_tipo'),
        verified_ultimo_momento = $('#id_ultimo_momento');

        function Verificar(value) {
            if(value == 1){
                verified_ultimo_momento.parent('div').show();
            }else{
                verified_ultimo_momento.parent('div').hide();
            }
        }

        Verificar(selectField.val());

        selectField.change(function() {
            Verificar($(this).val());
        }); 
    
    });

})(jQuery || django.jQuery);
    