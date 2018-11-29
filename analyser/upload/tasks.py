from analyser.celery import app


@app.task(bind=True)
def process_file(self, filename):
    print("Inside tasks")
    print(filename)
