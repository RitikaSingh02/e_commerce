angular.module("payment",[]).controller("payment_ctrl",function($scope,$http){
    $scope.errorMessage = false;
    $scope.subFunction=function(){
        
        var url="https://ifsc.razorpay.com/"+$scope.ifsc
        $http.get(url).then(function(response){
            
            if(response.data ){
                function makeid(length) {
                    var result           = '';
                    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
                    var charactersLength = characters.length;
                    for ( var i = 0; i < length; i++ ) {
                       result += characters.charAt(Math.floor(Math.random() * charactersLength));
                    }
                    return result;
                 }
                 
                
                data={"order_id":makeid(5),"email":$scope.em,"amount":$scope.amt}

                $http.post('http://127.0.0.1:8000/payment/payment1/', JSON.stringify(data)).then(function (response) {
                    if(response.data){
                        url = "https://securegw-stage.paytm.in/order/status";
                        $http.post(url, JSON.stringify(response.data)).then(function (response){
                                console.log(response.data);
                        })
                       
                    }

                
                
        });
    }
},function(){
    $scope.errorMessage = "invalid ifsc";
})
}
c=0
$scope.checked=function(){
    if($scope.location){
        if(c==0){
            if (navigator.geolocation) {
              navigator.geolocation.getCurrentPosition(showPosition);
              
              c=1
            function showPosition(position) {
                lat= position.coords.latitude;
                long= position.coords.longitude;
                url="https://api.opencagedata.com/geocode/v1/json?q="+lat+"+"+long+"&key=a5fa2cf59d734aa4a211a5d7061a21bf";
                console.log(url);
                $http.get(url).then(function(response){

                    $scope.addr=response.data['results'][0]['components']['residential']+','+
                    response.data['results'][0]['components']['county']+','+
                    response.data['results'][0]['components']['state_district']+','+
                    response.data['results'][0]['components']['state']+','+
                    response.data['results'][0]['components']['country'];
                    console.log($scope.addr)
                })
                }
            } else { 
              alert("geolocation is not supported enter manually")
            }
        }
        
    return false
    }
    else
    return true
}
d=0
$scope.checked_pin=function(){
    if($scope.pin_gen){
        if(d==0){
            if (navigator.geolocation) {
              navigator.geolocation.getCurrentPosition(showPosition);
              
              d=1
            function showPosition(position) {
                lat= position.coords.latitude;
                long= position.coords.longitude;
                url="https://api.opencagedata.com/geocode/v1/json?q="+lat+"+"+long+"&key=a5fa2cf59d734aa4a211a5d7061a21bf";
                console.log(url);
                $http.get(url).then(function(response){

                    $scope.pin=response.data['results'][0]['components']['postcode']
 
                    console.log($scope.pin);
                })
                }
            } else { 
              alert("geolocation is not supported enter manually")
            }
        }
        return false
    }
    else
    return true
}

}
);

