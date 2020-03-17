# Logistical changes, weeks 10-12

This page collects the various ways in which the delivery of this course will change during the last three weeks, following the university's decision to stop in-person classes, in response to the COVID-19 pandemic.

This page will be updated over time as more details are worked out.

## Communication methods

Our highest-bandwidth tool for communication will be the course discussion board on Piazza. Please continue to post questions there, and I will try to respond to them promptly. I will be posting announcements to Piazza. Important announcements will *also* continue to be posted to the 'Announcements' section of the course website.

As before, if you have a question about a private matter, you can send me an e-mail or post a private question on Piazza.

## Lectures

Our replacement for lectures will come in two parts:

### Weekly lecture recordings/readings

At the beginning of the week, I will post lecture recordings to the course website (alongside the normal raw and annotated slides). [This thread on Piazza](https://piazza.com/class/k4xo4w48g2u35e?cid=247) also gives readings from the Vassos course notes which cover the exact same material. You should do the readings **or** view the lecture recordings before Wednesday (though you don't need to do both!).

### Wednesday Q&A sessions

On Wednesdays from 12-2, I will hold **live Q&A sessions** using the 'BB Collaborate' tool on Quercus. My greatest wish is to receive lots of questions about the week's topic. If questions pop into your head as you're watching the recordings or doing the readings, please jot them down and we can discuss on Wednesday. If there is time, I will also be happy to discuss any of the following:

* The week's tutorial exercises
* Material from earlier in the course
* Course logistics (though if you have a question that's specific to your situation, you should ask in [office hours](#office-hours) instead)

You are welcome to drop in at any point during this two hour period (you don't need to limit yourself to the 1 hour during which you normally attend lecture).

## Tutorials

Tutorials will be held over BB Collaborate, but will otherwise be fairly similar to the previous format. On Friday at 12 or 1 (whenever you normally attend tutorial), you should head to Quercus, and look for the session being hosted by your normal TA (sessions will be labelled with the TA's name, and the corresponding tutorial room and surname range).

Quizzes will be given out by TAs at the end of the tutorial session. You will have the usual 10-15 minutes to write your answer, and you should then upload your solution to MarkUs within 10 minutes. Most submission formats will be accepted (including scanned, handwritten work). See the [Tests and quizzes via MarkUs](#tests-and-quizzes-via-markus) section below for further details.

## Office hours

I will hold office hours from Wednesday 2-4 via BB Collaborate. I'll chat with students 1-1 (in 'breakout rooms') in the order in which they arrive. If you're not available during this time but would still like to talk, please let me know and we can schedule a different time.

## Midterm 2

The second midterm was originally scheduled to be written in person on Monday March 16. It will **instead be written Monday March 23rd**. A pdf of the midterm will be posted to the course website at exactly 12:00 noon. You will have 50 minutes to write the test. If you have any clarifying questions, I will be available during this time to answer them either asynchronously (via private Piazza posts) or synchronously (via BB Collaborate).

At 12:50, you should collect your answers into an appropriate digital format and upload them to MarkUs. The test will be open book, but you should not consult any sources other than course materials. See the [Tests and quizzes via MarkUs](#tests-and-quizzes-via-markus) section below for more details on allowed submission formats.

If you will not be able to write the test at noon (due to conflict with another course, travel, illness, or any other reason), please send me an e-mail as soon as possible. (If you have a valid reason for missing the midterm, I will make sure it does not adversely affect your grade.)

### Midterm submission deadline

In the interest of fairness, your submission should be uploaded to MarkUs **no later than 13:00**. If you are writing the midterm on paper, we will allow an extra 10 minutes (i.e. you may submit up to 13:10), as we recognize that scanning papers takes extra time.

<!-- Other late submissions may be accepted in extraordinary circumstances, e.g. internet outage, cat hit the power button on your computer, etc. But try to take reasonable precautions (e.g. save your work frequently). -->
If you submit your work *in some form* within the time limit, it's fine to go back later and upload another version with cosmetic fixes (different resolution, cropped, rotated, etc.), but send me a quick heads-up if you do this.

If for some reason you experience technical difficulties with MarkUs, you can e-mail your work to me as a last resort ([colin@cs.toronto.edu](mailto:colin@cs.toronto.edu)). 

## Tests and quizzes via MarkUs

Tutorial quizzes and the second midterm will be written at home and submitted online through MarkUs. This section goes over some logistical details common to quizzes and the midterm.

### Submission format

You are welcome to use any medium for writing up your answers, as long as you can export it to a file that we can read in MarkUs. Our preference would be a pdf, but any plain text format is fine, as are most image files. Please avoid proprietary formats such as docx. Below are a few options for writing your solutions, along with some notes/caveats:

* Pen and paper
    * You can scan your work, or just take a photo with your phone. Try to make sure the image is in focus, and oriented properly. 
    * If your work spans multiple pages, it would greatly help us if you give the corresponding files names that indicate the order in which they should be read (e.g. 1.png, 2.png, 3.png etc.). It would be even better if you could join them into one pdf. ([This StackOverflow post](https://stackoverflow.com/questions/4778635/merging-png-images-into-one-pdf-file) gives a couple of one-liners for doing this, if you're comfortable using the command line and installing programs via your system's package manager.)
* Tablet / stylus
    * A great 'best of both worlds' option if you have the hardware
* Plain text files
    * It can be awkward to write proofs in ASCII without access to mathematical notation. If you go this route, aim for clarity over visual fidelity. 'Pidgin' LaTeX may be helpful here. For example, `forall A in N^*, P(A) AND Q(A)` is clearer than something like `\-/ A E |N*, P(A) /\ Q(A)`.
    * Unfortunately, when showing text files, MarkUs does not 'soft wrap' long lines (instead it creates a horizontal scrollbar). It would help us a lot if you could keep the lines of your text files no longer than, say, 120 characters. The following shell command will automatically 'hard wrap' the text file a.txt to have no more than 80 characters per line, writing the result to b.txt: `fold -s -w 80 a.txt > b.txt`. 
* LaTeX
    * Great if you can manage it, but will probably be significantly slower than other options unless you're a LaTeX master.
    * If you do go down this path and find you're having difficulties getting your document to compile as time is running out, you can always just submit the .tex file as a last resort.
* MS Word, Google Docs, or other word processors
    * These are fine. Just make sure to export to pdf at the end.


### Consulting resources during tests/quizzes

Midterm 2 and the remaining tutorial quizzes should be considered 'open book' in the sense that you may consult your own notes and any official course resources, including the course notes by Vassos Hadzilacos, lecture slides, tutorial exercises, and anything else uploaded to the course website.

But you should not consult any other online sources during tests and quizzes or collaborate with anyone else.

## Exam

We were originally scheduled to write a final exam worth 41% of the final grade. My current **tentative** plan is to distribute some of that 41% to existing term work (particularly the first midterm), and allocate some of it to a final 'take-home exam'. In terms of length and content, this would be similar to a normal 3-hour 236 exam, but you would have a few days to write it. Answers would be submitted to MarkUs (LaTeX not required). It would be released some time around our original exam date of April 7. As with the quizzes and second midterm, it would be open book, but with no collaboration or consultation of online sources (aside from course materials).

Note that any reweighting will need to be voted on by the class and receive majority approval to pass.

## Questions?

Please post them to Piazza so others can benefit from the answer as well. (Suggestions are also welcome! Much of this is uncharted territory, and I would very much appreciate any ideas you might have on how to make the most of these strange last three weeks.)
