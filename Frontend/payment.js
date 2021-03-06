angular.module("payment", []).controller("payment_ctrl", function ($scope, $http) {
    $scope.errorMessage = false;
    $scope.subFunction = function () {
        var order;
        var url = "https://ifsc.razorpay.com/" + $scope.ifsc
        $http.get(url).then(function (response) {

            if (response.data) {
                function makeid(length) {
                    var result = '';
                    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
                    var charactersLength = characters.length;
                    for (var i = 0; i < length; i++) {
                        result += characters.charAt(Math.floor(Math.random() * charactersLength));
                    }
                    return result;
                }

                order1 = makeid(5)
                order = order1;
                current_url = window.location.href;
                console.log(typeof(current_url));
                product_id = current_url.split('=')[1].split('?')[0];
                console.log(product_id)
                $scope.amt = current_url.split('?')[2].split('=')[1];
                data = { "order_id": order, "email": $scope.em, "amount": $scope.amt, "cust_id": sessionStorage.getItem('cust_id'), "product_id": product_id }

                $http.post('http://127.0.0.1:8000/payment/payment1/', JSON.stringify(data)).then(function (response) {
                    if (response.data) {
                        window.location.href = 'http://127.0.0.1:8000/payment/payload/' + order1 + '/'
                    }
                });
            }
        }, function () {
            $scope.errorMessage = "invalid ifsc";
        })
    }
    c = 0
    $scope.checked = function () {
        if ($scope.location) {
            if (c == 0) {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);

                    c = 1
                    function showPosition(position) {
                        lat = position.coords.latitude;
                        long = position.coords.longitude;
                        url = "https://api.opencagedata.com/geocode/v1/json?q=" + lat + "+" + long + "&key=00055960605c4ceeb008c196e125eb4d";

                        $http.get(url).then(function (response) {

                            $scope.addr = response.data['results'][0]['components']['residential'] + ',' +
                                response.data['results'][0]['components']['county'] + ',' +
                                response.data['results'][0]['components']['state_district'] + ',' +
                                response.data['results'][0]['components']['state'] + ',' +
                                response.data['results'][0]['components']['country'];

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
    d = 0
    $scope.checked_pin = function () {
        if ($scope.pin_gen) {
            if (d == 0) {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);

                    d = 1
                    function showPosition(position) {
                        lat = position.coords.latitude;
                        long = position.coords.longitude;
                        url = "https://api.opencagedata.com/geocode/v1/json?q=" + lat + "+" + long + "&key=00055960605c4ceeb008c196e125eb4d";
                        console.log(url);
                        $http.get(url).then(function (response) {

                            $scope.pin = response.data['results'][0]['components']['postcode']


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

