<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Tabla de multiplicar</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
    <script src="main.js"></script>
</head>
    <body bgcolor="#cfcfcf">
        <form action="quiz brayan rivera.php" method="POST">
            <center>
                    <table aling="center" border="4" height="120" width='120' align="center" background="/text/images/jhonny.jpg" no repeat>
                        <tr>
                            <td colspan="4"  >
                                <CEnter><B><H1>Tabla de Multiplicar</H1><br> </B></CEnter>
                            </td>
                        </tr>
                      

                    </table>
                </center>
        </form>
    </body>
</html>
<center>
<?php




echo "<table border = 2>";

//Le ponemos los titulos a las cabeceras de las columnas

echo "<th> Tabla * </th>";
echo "<th> 1 </th>";
echo "<th> 2 </th>";
echo "<th> 3 </th>";
echo "<th> 4 </th>";
echo "<th> 5 </th>";
echo "<th> 6 </th>";
echo "<th> 7 </th>";
echo "<th> 8 </th>";
echo "<th> 9 </th>";
echo "<th> 10 </th>";

//mediante dos bucles "for" crearemos las filas de la columnas de forma dinámica

    for($i=1;$i<=10;$i++){
		 
		}
		echo "</tr>";
		echo "</thead>";
		echo "<tbody>";
		for($i=1;$i<=10;$i++){
			echo"<tr><th>".$i."</th>";
			for($j=1;$j<=10;$j++){
				$resultado=$i*$j;
				if($resultado%2==0 && $resultado%3!=0){
					echo"<td bgcolor='yellow'>".$resultado."</td>";
				}else if($resultado%2!=0 && $resultado%3!=0){
					echo"<td bgcolor='green'>".$resultado."</td>";
				}else if($resultado%3==0){
					echo"<td bgcolor='blue'>".$resultado."</td>";
				}
				
			}
            echo"</tr>";
        }
 
//cerramos la etiqueta table

echo "</table>";


?>
</center>