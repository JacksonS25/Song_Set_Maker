# Song Set Maker
A program that will take your Chord Sheet PDF's merger them into a single PDF and email them to you.

## Motivation
I hated the hassle of copying and pasting on my IPAD in pages to merge my chord sheets into a single easy to use set list.
The formatting would mess up during transfer and the songs were tedious to access and merge.
This program solves all of it by allowing you to type one line of code in the terminal to have your set list made and emailed to you for use on any device.

## Quick Start
1. You can download the repo and make sure the pypdf library is installed. If not, use:
   ```pip install pypdf```
3. Update the email and password field in email.py. For a gmail you will need an app password that you can get instructions for from a quick google search.
4. Add your own songs in pdf format to the songs directory or use the ones included.
5. Run ```bash song_set_maker.sh "song name" "song name" ... "output_pdf_name"```

## Future Features
- A docx to pdf converter to increase file compatibility and ease of use.
- A song directory search function to allow you to search through the songs for certain lyrics and returning a list of song names. For the days you can't quite remember the name of *that song*.

## 🤝 Contributing

### Clone the repo

```bash
git clone https://github.com/JacksonS25/Song_Set_Maker
cd Song_Set_Maker
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
