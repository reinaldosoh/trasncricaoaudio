<?php

$query = base64_decode($argv[1]);
$search_url = "https://ddg-api.herokuapp.com/search?query=" . urlencode($query) . "&limit=1";

try {
    $response = file_get_contents($search_url);
    if ($response === false) {
        die(base64_encode("No Result!"));
    }
    
    $data = json_decode($response, true);
    if (empty($data) || !isset($data[0]['body'])) {
        die(base64_encode("No Result!"));
    }
    
    die(base64_encode($data[0]['body']));
} catch (Exception $e) {
    die(base64_encode("Erro na busca: " . $e->getMessage()));
}

?>
