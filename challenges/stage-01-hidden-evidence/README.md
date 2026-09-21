# Stage 01 – Hidden Evidence

## Domain
Steganography

## Difficulty
Easy

## Scenario
During the initial investigation of the NovaTech Solutions incident, an image named `nova-office.jpeg` was recovered from suspicious internal activity. The image appears normal, but investigators believe that it contains hidden information left by the attacker.

## Learning Objective
Identify and extract data hidden inside an image using basic steganography analysis techniques.

## Player Task
Analyze the provided `nova-office.jpeg` file and recover the hidden information.

## Challenge File
`files/nova-office.jpeg`

## Suggested Tools
- file
- exiftool
- strings
- binwalk
- steghide

## Expected Approach
1. Identify the supplied file type.
2. Inspect the image and its metadata.
3. Perform steganography analysis.
4. Detect the embedded file.
5. Extract the hidden payload.
6. Recover the Stage 01 flag and clue for the next stage.

## Flag Format
`SHADOW{...}`

## Progression
Successfully extracting the hidden payload reveals the Stage 01 flag and directs the participant to investigate the coded message in Stage 02.

## Reset / Recovery
This is a static challenge. No container or service reset is required. The original challenge image can simply be redistributed through CTFd if required.
