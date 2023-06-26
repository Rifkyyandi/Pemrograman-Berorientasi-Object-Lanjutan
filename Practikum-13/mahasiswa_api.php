<?php
require_once 'database.php';
require_once 'Mahasiswa.php';
$db = new MySQLDatabase();
$mahasiswa = new Mahasiswa($db);
$id=0;
$nim=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        if($id>0){    
            $result = $mahasiswa->get_by_id($id);
        }elseif($nim>0){
            $result = $mahasiswa->get_by_nim($nim);
        } else {
            $result = $mahasiswa->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new mahasiswa
        $mahasiswa->nim = $_POST['nim'];
        $mahasiswa->nama = $_POST['nama'];
        $mahasiswa->jk = $_POST['jk'];
        $mahasiswa->prodi = $_POST['prodi'];
       
        $mahasiswa->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mahasiswa created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mahasiswa not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $mahasiswa->nim = $_PUT['nim'];
        $mahasiswa->nama = $_PUT['nama'];
        $mahasiswa->jk = $_PUT['jk'];
        $mahasiswa->prodi = $_PUT['prodi'];
        if($id>0){    
            $mahasiswa->update($id);
        }elseif($nim<>""){
            $mahasiswa->update_by_nim($nim);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mahasiswa updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mahasiswa update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        if($id>0){    
            $mahasiswa->delete($id);
        }elseif($nim>0){
            $mahasiswa->delete_by_nim($nim);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mahasiswa deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mahasiswa delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>