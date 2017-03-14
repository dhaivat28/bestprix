<?php
   $db = new mysqli('localhost', 'root' ,'', 'bestprix');
	
	if(!$db) {
	
		echo 'Could not connect to the database.';
	} else {
	
		if(isset($_POST['queryString'])) {
			$queryString = $db->real_escape_string(trim($_POST['queryString']));			
			if(strlen($queryString) >0) {

				$query = $db->query("SELECT distinct name FROM snapdeal_data WHERE name LIKE '$queryString%'");
				if($query) {
				echo '<ul>';
					while ($result = $query ->fetch_object()) {
	         			echo '<li onClick="fill(\''.addslashes($result->name).'\');">'.$result->name.'</li>';
	         		}
				echo '</ul>';
					
				} else {
					echo 'OOPS we had a problem :(';
				}
			} else {
				// do nothing
			}
		} else {
			echo 'There should be no direct access to this script!';
		}
	}
?>