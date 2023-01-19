<?php
/*
 * Project     : ex-db-con
 * Script      : database.inc.php
 * Description : Database connector
 * Author      : DOMINGUES PEDROSA Samuel
 * Date        : 2023.01.19, V1.0
 */

// Database constants
define("HOST", "localhost");
define("DBNAME", "scale");
define("USER", "scaler");
define("PASSWORD", "heft");

class DatabseController{
    private $db = null;
    private $psInsert = null;

    public function __construct()
    {
        if ($this->db == null) {
            try {
                // Create database PDO
                $this->db = new PDO('mysql:host=' . HOST . ';dbname=' . DBNAME, USER, PASSWORD, array(
                    PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8",
                    PDO::ATTR_PERSISTENT => true
                ));

                // Insert
                $sql = 'INSERT INTO `weight` (`time`, `value`) VALUES (:TIME, :VALUE);';
                $this->psInsert = $this->db->prepare($sql);



            } catch (PDOException $e) {
                die("Erreur !: " . $e->getMessage() . "<br/>");
            }
        }
    }

    /**
     * Insert
     * @param mixed $val1
     * @param mixed $valn
     * @return bool
     */
    function insert($time, $value){
        $result = null;
        try {
            $this->psInsert->bindParam(':TIME', $time, PDO::PARAM_STR);
            $this->psInsert->bindParam(':VALUE', $value);
            if ($this->psInsert->execute()){
                $result = $this->psLastId->execute();
            }
        } catch (PDOException $e) {
            die("Erreur !: " . $e->getMessage() . "<br/>");
        }
        return $result;
    }
}
?>