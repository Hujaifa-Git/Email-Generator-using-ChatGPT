from flask import Flask, render_template, request
import config as ctg
import openai

def page_not_found(e):
  return render_template('404.html'), 404


def getresponse(prompt):
    api_key = ctg.OPENAI_API_KEY
    endpoint = 'https://api.openai.com/v1/'

    openai.api_key = api_key
    openai.api_base = endpoint

    # Make a request to the API
    response = openai.Completion.create(
        engine="text-davinci-003",  # You may use a different engine, check the latest available engines
        prompt=prompt,
        max_tokens=150
    )

    # Extract and print the generated text
    generated_text = response['choices'][0]['text']
    return generated_text

app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/schedule-meeting', methods=["GET", "POST"])
def schedulemeeting():

    if request.method == 'POST':
        name = request.form['schedule-meeting-name']
        reason = request.form['schedule-meeting-reason']
        time = request.form['schedule-meeting-time']
        prompt = f'Compose an email to schedule a meeting with {name} to discuss {reason} at {time}.'
        openAIAnswer = getresponse(prompt)
        # openAIAnswer = prompt
    return render_template('schedule-meeting.html', **locals())

@app.route('/follow-up', methods=["GET", "POST"])
def followup():

    if request.method == 'POST':
        your_name = request.form['follow-up-your-name']
        your_organization = request.form['follow-up-your-organization']
        client_name = request.form['follow-up-client-name']
        client_organization = request.form['follow-up-client-organization']
        your_service = request.form['follow-up-your-service']
        your_service_benefit = request.form['follow-up-your-service-benefit']
        

        prompt = f'I’m the {your_name} from {your_organization} . Write a persuasive follow-up email to {client_name} from {client_organization} who expressed interest in our {your_service}. The benefits we offer are, {your_service_benefit}. Keep it under 150 words.'
        openAIAnswer = getresponse(prompt)

    return render_template('follow-up.html', **locals())

@app.route('/request-something', methods=["GET", "POST"])
def requestsomething():

    if request.method == 'POST':
        name = request.form['request-something-name']
        reason = request.form['request-something-reason']

        prompt = f'Draft an email to {name} asking for {reason}'
        openAIAnswer = getresponse(prompt)

    return render_template('request-something.html', **locals())


@app.route('/project-update', methods=["GET", "POST"])
def projectupdate():

    if request.method == 'POST':
        name = request.form['project-update-name']
        project_name = request.form['project-update-project-name']
        updates = request.form['project-updates']
        prompt = f'Create an email updating {name} on the status of {project_name}, including {updates}'
        openAIAnswer = getresponse(prompt)

    return render_template('project-update.html', **locals())

@app.route('/summarize', methods=["GET", "POST"])
def summarize():

    if request.method == 'POST':
        email = request.form['summarize-mail']
        
        prompt = f'Summarize the main points of this email into bullet points, {email}'
        openAIAnswer = getresponse(prompt)

    return render_template('summarize.html', **locals())

@app.route('/payment-reminder', methods=["GET", "POST"])
def paymentreminder():

    if request.method == 'POST':
        name = request.form['payment-reminder-name']
        service = request.form['payment-reminder-service']
        amount = request.form['payment-reminder-amount']
        date = request.form['payment-reminder-date']
        
        prompt = f'Write an email to {name}, attaching their invoice for {service} for the total amount of {amount} and kindly reminding them the due date for payment is {date}'
        openAIAnswer = getresponse(prompt)

    return render_template('/payment-reminder.html', **locals())

@app.route('/apologize', methods=["GET", "POST"])
def apologize():

    if request.method == 'POST':
        name = request.form['apologize-name']
        why = request.form['apologize-why']
        reason = request.form['apologize-reason']

        prompt = f'Write an Email to {name} apologizing about {why}. The reason is, {reason}'
        openAIAnswer = getresponse(prompt)

    return render_template('/apologize.html', **locals())

@app.route('/refferal', methods=["GET", "POST"])
def refferal():

    if request.method == 'POST':
        service = request.form['refferal-service']
        prompt = f'We are a {service} service company. Compose an email to a satisfied client asking if they would be willing to provide a testimonial for our website or refer us to their contacts.'
        openAIAnswer = getresponse(prompt)

    return render_template('/refferal.html', **locals())

@app.route('/decline-invitation', methods=["GET", "POST"])
def declineinvitation():

    if request.method == 'POST':
        name = request.form['decline-invitation-name']
        reason = request.form['decline-invitation-reason']
        
        prompt = f'Draft a polite and professional email to decline a {name}, expressing gratitude for the opportunity and explaining you can’t make it due to {reason}'
        openAIAnswer = getresponse(prompt)

    return render_template('/decline-invitation.html', **locals())

@app.route('/job-application', methods=["GET", "POST"])
def jobapplication():

    if request.method == 'POST':
        name = request.form['job-application-name']
        organization = request.form['job-application-organization']
        position = request.form['job-application-position']
        name2 = request.form['job-application-name2']

        prompt = f'My name is {name}. Compose a job application email for the position of {position} at {organization}, showing enthusiasm for the role and the company, and an attachment of your resume. Maintain a professional and engaging tone, addressing the email to the hiring manager {name2} and including a call-to-action to schedule an interview.'
        openAIAnswer = getresponse(prompt)

    return render_template('/job-application.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)