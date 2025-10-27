# AWS_IVR_Project
Developed a cloud-based IVR system using Amazon Connect, Lex, Lambda, and DynamoDB. Designed intelligent call flows with voice-based option selection, automated call routing, and scalable serverless deployment to improve customer service efficiency and reduce manual effort.


# 🗣️ Amazon Lex Bots – Aadhaar, Phone Number & Balance Assistant

This repository contains the exported configurations for a set of **Amazon Lex V2 chatbots** designed to handle simple user queries such as retrieving Aadhaar details, phone number, and checking account balance.  

All bots are **basic versions** without Lambda code hooks — designed primarily for demonstration, testing, and educational use.

---

## 🤖 Bots Overview

### 🧠 1. AadhaarPhoneBot
**Platform:** Amazon Lex V2  
**Type:** Basic (no Lambda code hooks)  
**Language:** English (en-IN)  
**Purpose:** Provides a conversational interface for users to get their Aadhaar number or phone number.  

#### Intents
##### `GetAadhaar`
Handles user queries related to retrieving or confirming their Aadhaar number.

**Example Utterances:**
- "What is my Aadhaar number?"
- "Can you tell me my Aadhaar?"
- "I want my Aadhaar details."

**Response Example:**
> “Sure, please provide your registered details so I can help you with your Aadhaar number.”

##### `GetPhoneNumber`
Handles user queries related to retrieving or confirming their phone number.

**Example Utterances:**
- "Tell me my phone number."
- "What’s my registered number?"
- "Can I get my mobile number details?"

**Response Example:**
> “Your registered phone number ends with ****1234.”

---

### 💰 2. BalanceCheckBot
**Platform:** Amazon Lex V2  
**Type:** Basic (no Lambda code hooks)  
**Language:** English (en-IN)  
**Purpose:** Allows users to check their account balance using simple voice or text interactions.

#### Intents
##### `CheckBalance`
Handles user queries about their account balance.

**Example Utterances:**
- "What’s my account balance?"
- "Check my balance."
- "How much money do I have?"

**Response Example:**
> “Your current account balance is ₹5,000.”

---

## 📁 Repository Structure




---

## 🚀 How to Import into AWS Lex

1. Open the **Amazon Lex Console**.  
2. Choose **Create bot → Import**.  
3. Upload the `bot.json` file from the desired bot folder (e.g., `AadhaarPhoneBot/bot.json`).  
4. After import, confirm that all intents and utterances appear correctly.  
5. Build and test the bot directly in the Lex console.

---

## 🧠 Future Enhancements
- Add **Lambda code hooks** for dynamic data retrieval (Aadhaar, phone number, and account balance).  
- Connect with **external APIs or databases** for real-time responses.  
- Enable **multi-turn conversations** for improved engagement.  
- Integrate **Amazon Connect** for IVR-style voice experiences.  
- Implement **version control for multiple bot iterations** (v1, v2, etc.).

---

## 👨‍💻 Author
**Arpan Dasgupta**  
*Data & AI Enthusiast | Machine Learning | AWS | Backend Development*

---



