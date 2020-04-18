<?php
	$ip = $_GET['ip'];
	$port = $_GET['port'];
	$scheme = $_GET['scheme'];
	$data = $_GET['data'];
	echo $scheme;

	header("Location: $scheme://$ip:$port/$data");
?>