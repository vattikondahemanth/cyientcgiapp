<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>

<script>
$(document).ready(function(){
 
  $("#btn").click(function(){
       var form = $("#formId");
      

        $.post(


                {

                  url: "http://localhost:8080/cgi-bin/login/login.py",
                  type: "POST",
                  data: form.serialize(),
                  success: function(result){
                      console.log(result.trim());
                      result = JSON.parse(result);
                      $("#div1").html(result['a']);                
                     
                  },
                  error: function(result){
                    console.log("Hemanth")
                  }





                }



            );


  });



});
</script>