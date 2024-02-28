{% load static %}
<!DOCTYPE html>
<html lang="en" data-wf-page="65bde29e6cc1fd5bbc32b14e" data-wf-site="65bd3247074aa3f2dc61ee46">
<head>
    <meta charset="utf-8">
    <title>Sign Up</title>
    <meta content="Sign Up" property="og:title">
    <meta content="Sign Up" property="twitter:title">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta content="Webflow" name="generator">
    <link href="{% static 'css/normalize.css' %}" rel="stylesheet" type="text/css">
    <link href="{% static 'css/webflow.css' %}" rel="stylesheet" type="text/css">
    <link href="{% static 'css/ask-a-philosopher-39be2e.webflow.css' %}" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com" rel="preconnect">
    <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
    <script type="text/javascript">WebFont.load({  google: {    families: ["Inter:100,200,300,regular,500,600,700,800,900"]  }});</script>
    <script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script>
    <link href="{% static 'images/favicon.ico' %}" rel="shortcut icon" type="image/x-icon">
    <link href="{% static 'images/webclip.png' %}" rel="apple-touch-icon">
</head>
<body class="body-2">
    <section class="section-2">
        <div class="w-layout-blockcontainer container-3 w-container">
            <a href="{% url 'home' %}" class="w-inline-block"><img src="{% static 'images/headofgreekphilosophersocratesfromathensmonolineillustrationvector3690609693-32x.png' %}" loading="lazy" width="94" alt="" class="image-12"></a>
        </div>
    </section>
    <div class="w-layout-blockcontainer w-container">
        <h1 class="heading-2">Create your account</h1>
        <div class="w-form">
            <form id="register-form" name="register-form" method="post" action="" class="form-2">
                {% csrf_token %}
                <input class="text-field-2 w-input" maxlength="256" name="{{ form.email.name }}" placeholder="Email address" type="email" id="email" required>{{ form.email.errors }}
                <input class="text-field-3 w-input" maxlength="256" name="{{ form.password1.name }}" placeholder="Password" type="password" id="password1" required>{{ form.password1.errors }}
                <input class="text-field-3 w-input" maxlength="256" name="{{ form.password2.name }}" placeholder="Confirm Password" type="password" id="password2" required>{{ form.password2.errors }}
                <input type="submit" data-wait="Please wait..." class="submit-button w-button" value="Continue">
            </form>
            <div class="w-form-done">
                <div>Thank you! Your submission has been received!</div>
            </div>
            <div class="w-form-fail">
                <div>Oops! Something went wrong while submitting the form.</div>
            </div>
        </div>
        <div class="text-block-5">Already have an account? <a href="{% url 'login' %}" class="link">Log In</a></div>
    </div>
    <script src="{% static 'js/jquery-3.5.1.min.dc5e7f18c8.js' %}" type="text/javascript"></script>
    <script src="{% static 'js/webflow.js' %}" type="text/javascript"></script>
</body>
</html>
