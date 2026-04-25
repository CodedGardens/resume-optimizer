from app.resume_parser import ResumeParser

parser = ResumeParser("TestingTesting.pdf")
text = parser.extractText()

print(text[:1000])