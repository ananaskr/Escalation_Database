Hello , Try to SSRF

<?php
	if(isset($_GET['url'])){
		$link = $_GET['url'];
		$curlobj = curl_init();
		curl_setopt($curlobj, CURLOPT_POST,0);
		curl_setopt($curlobj, CURLOPT_URL,$link);
		curl_setopt($curlobj, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($curlobj, CURLOPT_FOLLOWLOCATION, 1);
		$result=curl_exec($curlobj);
		echo $result;
		curl_close($curlobj);
	}
?>