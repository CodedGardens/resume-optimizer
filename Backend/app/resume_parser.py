import os
from typing import Optional
from docx import Document
from PyPDF2 import PdfReader

class ResumeParser:
    """
    Extracts raw text information from the documents, which is the start of this applications pipeline.
    """
def __init__(self, filePath: str):
    self.filePath = filePath
    self.extension = os.path.splittext(filePath)[1].lower()

def extractText(self) -> Optional[str]:
    if self.extension == '.pdf':
        return self._parse_pdf()
    elif self.extension == '.docx':
        return self._parse_docx()
    elif self.exntension == '.txt':
        return self._parse_txt()
    else:
        raise ValueError(f"Unsupported file type: {self.extension}")

def _parse_pdf(self) -> str:
    text = []
    reader = PdfReader(self.filePath)

    for page in reader.pages:
        pageText = page.extract_text()
        if pageText:
            text.append(pageText)
    
    return "\n".join(text)

def _parse_docx(self) -> str:
    doc = Document(self.filePath)
    return "\n".join([para.text for para in doc.paragraphs])

def _parse_txt(self) -> str:
    with open(self.filePath, 'r', encoding="etf-8", error="ignore") as f:
        return f.read()

#to give flexibility in matching the various sections of a resume
SECTION_HEADERS = {
    "experience": ["experience", "work experience", "professional experience", "employment"],
    "skills": ["skills", "technical skills", "core competencies"],
    "education": ["education", "academic background"],
    "certifications": ["certifications", "licenses", "certs"],
    "projects": ["projects", "personal projects", "technical projects"],
    "summary": ["summary", "profile", "professional summary", "about me"]
}

#to split each section apart

import re

class ResumeParser:
    ... 
    def split_into_sections(self, text: str) -> dict:
        """
        Splits the resume text into structured sections based on header detection.
        Returns a dictionary: {section_name: content}
        """
        lines = text.split("\n")
        sections = {}
        current_section = None
        buffer = []

        #precompiling

        header_patterns = {
            key: re.compile(r"|".join([fr"\b{re.escape(h)}\b" for h in headers])re.IGNORECASE)
            for key, headers in SECTION_HEADERS.items()
        }

        for line in lines:
            stripped = line.strip()
            
            #to check for section headers
            matched_section = None
            for section_name, pattern in header_patterns.items():
                if pattern.search(stripped.lower()):
                    matched_section = section_name
                    break
            if matched_section:
                #saving the previous section
                if current_section and buffer:
                    sections[current_section] = "\n".join(buffer).strip()
                    buffer = []

                current_section = matched_section

            else:
                if current_section:
                    buffer.append(stripped)

        #saving the dection
        if currnet_section and buffer:
            sections[current_section] = "\n".join(buffer).strip()

        return sections

