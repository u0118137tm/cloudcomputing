<?php

include("connect.php");



	
$sql = "CREATE TABLE professions (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    profession varchar(255),
    PRIMARY KEY (id));";

if ($conn->query($sql) === TRUE) {
	echo "De query werd succesvol uitgevoerd";
} 
else {
	echo "Error: " . $sql . "<br>" . $conn->error;
}

	
$conn->close(); 

?>
