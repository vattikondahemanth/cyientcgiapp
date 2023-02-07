<script>
$(document).ready(function(){
 
  $("#btn").click(function(){
      

        $.ajax(


                {

                  url: "http://localhost:8080/cgi-bin/login/login.py", 
                  success: function(result){
                   
                    console.log(result)                   
                     
                  },
                  error: function(result){
                    console.log("Hemanth")
                  }





                }



            );


  });



});
</script>