var YSLATE = {};

YSLATE.common = (function() {
	var init = function() {
		// common init
	}

	return {
		init: init
	};
}());

YSLATE.mobile = (function() {
	var directionsDisplay;
	var init = function() {
		//alert ( $(window).width() );
		directionsDisplay = new google.maps.DirectionsRenderer();
		setupMap();
		calcRoute();
		
	};
	
	

	var setupMap = function() {

		var mapOptions = {
			center : new google.maps.LatLng(-34.397, 150.644),
			zoom : 16,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		};
		var address = window.SLATELOCATION;
		var map = new google.maps.Map(document.getElementById("mapCanvas"), mapOptions);
		var geocoder = new google.maps.Geocoder();
		directionsDisplay.setMap(map);
		
        geocoder.geocode( { 'address' : address }, showSinglePoint);

        function showSinglePoint(results, status) {
			if (status == google.maps.GeocoderStatus.OK) {
				map.setCenter(results[0].geometry.location);
				var marker = new google.maps.Marker({
				    map: map,
				    position: results[0].geometry.location
				});
			} else {
				console.log('Geocode was not successful for the following reason: ' + status);
			}
        }
	};
	
	function calcRoute() {
		success = function(data) {
			var latLong = new google.maps.LatLng(data.coords.latitude, 
												 data.coords.longitude);
			var directionsService = new google.maps.DirectionsService();
			var start = latLong;
			var end = "16 Adelaide Street Boston MA 02130";
			var request = {
					origin : start,
					destination : end,
					travelMode : google.maps.TravelMode.WALKING
			};
			directionsService.route(request, function(result, status){
				if (status == google.maps.DirectionsStatus.OK){
					directionsDisplay.setDirections(result);
				}
			});
			alert(latLong)
		};
		var failure = function(error){
			alert( "could not get location");
		};
		navigator.geolocation.getCurrentPosition(success, failure, {timeout : 5000});
	};
	
	
	

	return {
		init: init
	};

}());

YSLATE.printable = (function() {

	var init = function() {
		setupMap();
	};

	var setupMap = function() {

		var mapOptions = {
			center : new google.maps.LatLng(-34.397, 150.644),
			zoom : 16,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		};
		var address = window.SLATELOCATION;
		var map = new google.maps.Map(document.getElementById("mapCanvas"), mapOptions);
		var geocoder = new google.maps.Geocoder();
		
        geocoder.geocode( { 'address' : address }, showSinglePoint);

        function showSinglePoint(results, status) {
			if (status == google.maps.GeocoderStatus.OK) {
				map.setCenter(results[0].geometry.location);
				var marker = new google.maps.Marker({
				    map: map,
				    position: results[0].geometry.location
				});
			} else {
				console.log('Geocode was not successful for the following reason: ' + status);
			}
        }

	};

	return {
		init: init
	};

}());

$(function() {
	window.UTIL = {

		fire : function (func,funcname, args) {

			// change this to whatever your namespace is actually called
			var namespace = YSLATE;

			// if funcname is undefined, we'll fire namespace.funcname.init()
			funcname = (funcname === undefined) ? 'init' : funcname;

			// if func exists, and namespace.func.funcname is a function...
			if (func !== '' && namespace[func] && $.isFunction(namespace[func][funcname])) {

				// call the method with optional arguments
				namespace[func][funcname](args);
			}

		},

		loadEvents : function () {
			var $body = $('body') || $(window.frames[0].document).find('body'),
			initClass = $body.data("init"),
			classMethod = $body.data("subinit");


			// hit namespace.common.init() first
			UTIL.fire('common');

			// fire namespace.initClass.classMethod()
			UTIL.fire(initClass,classMethod);

			// fire namespace.common.finalize() last (for code to always run after page initialization)
			UTIL.fire('common','finalize');

		}
	};
}(jQuery));


$(document).ready(UTIL.loadEvents);