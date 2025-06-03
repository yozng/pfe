<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="src/img/logo.jpg" type="image/png">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <!-- CSS -->
    <link rel="stylesheet" href="src/style.css">
    <title>Se connecter & S'inscrire</title>
</head>
<body>
    <div class="wrapper">
        <div class="form-header">
            <div class="titles">
                <div class="title-login">Se connecter</div>
                <div class="title-register">S'inscrire</div>
            </div>
        </div>
        <!-- LOGIN FORM -->
        <form action="#" class="login-form" autocomplete="off">
            <div class="input-box">
                <input type="text" class="input-field" id="log-email" required>
                <label for="log-email" class="label">Nom d'utilisateur :</label>
                <i class='bx bx-envelope icon'></i>
            </div>
            <div class="input-box">
                <input type="password" class="input-field" id="log-pass" required>
                <label for="log-pass" class="label">Mot de passe :</label>
                <i class='bx bx-lock-alt icon' ></i>
            </div>
            <div class="form-cols">
                <div class="col-1"></div>
           </div>
            <div class="input-box">
                <button class="btn-submit" id="SignInBtn">Se connecter <i class='bx bx-log-in' ></i></button>
            </div>
            <div class="switch-form">
                <span>Vous n'avez pas de compte ? <a href="#" onclick="registerFunction()">S'inscrire</a></span>
            </div>
        </form>

        <!-- REGISTER FORM -->
        <form action="#" class="register-form" autocomplete="off">
            <div class="input-box">
                <input type="text" class="input-field" id="reg-name" required>
                <label for="reg-name" class="label">Nom d'utilisateur :</label>
                <i class='bx bx-user icon' ></i>
            </div>
            <div class="input-box">
                <input type="text" class="input-field" id="reg-email" required>
                <label for="reg-email" class="label">Email :</label>
                <i class='bx bx-envelope icon'></i>
            </div>
            <div class="input-box">
                <input type="password" class="input-field" id="reg-pass" required>
                <label for="reg-pass" class="label">Mot de passe :</label>
                <i class='bx bx-lock-alt icon' ></i>
            </div>
            <div class="form-cols">
               <div class="col-1"></div>
            </div>
            <div class="input-box">
                <button class="btn-submit" id="SignUpBtn">S'inscrire <i class='bx bx-user-plus' ></i></button>
            </div>
            <div class="switch-form">
                <span>Vous avez déjà un compte ? <a href="#" onclick="loginFunction()">Se connecter</a></span>
            </div>
        </form>
    </div>

    <script src="src/script.js"></script>
</body>
</html>
