from bottle import Bottle, template, request
import roll

index_html = '''
<html>
  <head>
      <title>Bottleroller</title>
      
      <style>
        .footer {
          position: fixed;
          left: 0;
          bottom: 0;
          width: 100%;
          text-align: center;
        }

        p {font-family: Arial, Helvetica, sans-serif;}
      </style>
  </head>
  <body>
    <form method="post" action="/">
        <fieldset>
            <legend>SAMPLE FORM</legend>
            <ul>
                <li>Dice: <input name='dice'>
                </li>
            </ul><input type='submit' value='Throw Dice'>
        </fieldset>
    </form>
    
    <p><b>Example: 2d8 +6 +d8</b></p>
    
    <p><b>Your Throw:</b> {{throw}}</p>
    <p>{{result}}</p>

  </body>

  <div class="footer">
    <p>Based on Dice-Roller by <a href="https://gitlab.xirion.net/vroest/dice-roller">Victor Roest</a><br>
    <a href="https://github.com/metasikander/bottleroller">Github page</a></p>
  </div> 
</html>
'''

app = Bottle()

@app.route('/')
def index():
    """Home Page"""

    return template(index_html, result="Result here", throw=None)

@app.route('/', method="POST")
def formhandler():
    """Handle the form submission"""

    dice = request.forms.get('dice')

    result = "Result: " + str(roll.dice_roller(dice))

    return template(index_html, result=result, throw=dice)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, server='gunicorn', workers=4, debug=True)

# Found bugs:
# - no input in the form results in an error

#TODO:
# - Formatting of result
