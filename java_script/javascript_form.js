<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JavaScript Form Example</title>
    </head>

    <body>
        <h1>Sign Up Form</h1>
        <form id="signupForm">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br><br>
            <button type="submit">Submit</button>
        </form>
        <script>
            const form = document.getElementById("signupForm");

            form.addEventListener("submit", function (event) {

                event.preventDefault();

                const name = document.getElementById("name").value;

                const email = document.getElementById("email").value;

                if (name === "" || email === "") {

                    alert("Please fill in all fields.");

                    return;

                }

                alert(`Thank you for signing up, ${name}! We will send a confirmation to ${email}.`);

                form.reset();

            });

        </script>
    </body>

</html>
