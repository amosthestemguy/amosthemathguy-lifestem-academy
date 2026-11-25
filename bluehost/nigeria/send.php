<?php
// Receives a "For Nigerian Schools" interest request and emails it to support.
// Upload this file next to index.html on Bluehost. It uses PHP mail(), which Bluehost supports.
header('Content-Type: application/json; charset=utf-8');

$TO = 'support@countingtocalculus.org';
$FROM = 'noreply@' . preg_replace('/^www\./', '', $_SERVER['HTTP_HOST'] ?? 'countingtocalculus.org');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }
if (!empty($_POST['website'])) { echo '{"ok":true}'; exit; }          // spam trap: real people leave it empty

$clean = function ($v, $max) { $v = trim((string)$v); $v = str_replace(["\r", "\0"], '', $v); return mb_substr($v, 0, $max); };
$subject = preg_replace('/[\r\n]+/', ' ', $clean($_POST['subject'] ?? '', 200));
$body    = $clean($_POST['body'] ?? '', 8000);
$replyTo = filter_var($clean($_POST['email'] ?? '', 200), FILTER_VALIDATE_EMAIL);

if ($subject === '' || $body === '' || (stripos($subject, 'Book interest pledge') !== 0 && stripos($subject, 'School demo request') !== 0 && stripos($subject, 'Question before ordering') !== 0)) { http_response_code(400); echo '{"ok":false,"error":"missing"}'; exit; }

$headers = "From: Counting to Calculus <{$FROM}>\r\n";
if ($replyTo) { $headers .= "Reply-To: {$replyTo}\r\n"; }
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

$sent = mail($TO, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body . "\n\n-- Sent from " . ($_SERVER['HTTP_HOST'] ?? '') . " on " . gmdate('Y-m-d H:i') . " UTC", $headers);
echo json_encode(['ok' => (bool)$sent]);
