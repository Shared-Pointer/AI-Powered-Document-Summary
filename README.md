# 🦄 KakaSummary - Silly AI Doc Crusher

*"Because reading is for nerds, summarizing is for cool kids"* - Sun Tzu probably

## 🎪 What's this circus about?
A magical AI that turns your boring long documents into... slightly less boring short documents! Powered by Azure's brain juice and student tears.

---

## ~~🧙‍♂️ Abra-kadabra Setup (Azure Edition)~~

### ~~Numero uno - Azure Voodoo~~
1. ~~Get your student 🎓 email ready~~
2. ~~Go to [Azure Portal](https://portal.azure.com) (yes, the cloud place)~~
3. ~~Type `Language Service` like you're summoning a demon 🔮~~

### ~~Numero dos - Resource Goofin'~~
~~Fill this bad boy like:~~
- ~~**Subscription**: "Azure for Students" (the free candy 🍭)~~
- ~~**Resource group**: `AI-Document-Summary` (or whatever)~~
- ~~**Region**: West Europe 🌍 (or pick your favorite)~~
- ~~**Name**: `kaka-doc-summary-ai` (mandatory "kaka" prefix)~~
- ~~**Pricing tier**: F0 (aka "please don't charge me" mode)~~

### ~~Numero tres - Secret Sauce 🕵️~~
~~After Azure stops judging your life choices:~~
1. ~~Go to "Keys and Endpoint" (sounds spy-ish)~~
2. ~~Create `.env` file in `config/` with:~~

It doesn't work, we used the wrong AI :( and Azure for Students doesn't let us access the OpenAI model.

We can only use a special model to summarize text files, but this Azure service just copies and pastes random sentences from our text.
```ini
AZURE_ENDPOINT='https://kaka-doc-summary-ai.cognitiveservices.azure.com/'
AZURE_API_KEY='your-magic-code-here'
API_VERSION='2023-04-01'
MAX_TOKENS=1000
```

## 🚀 Launch Protocol (for dummies)
### Option A: Docker Magic 🐳
```
make build  # Wait for the robot to think
make run    # Unleash the beast
```
Then point browser to http://localhost:8501 and pray 🙏

### Option B: Manual Mode 🤓 (nerd)
```
pip install -r requirements.txt  # Download internet
streamlit run app/main.py       # Do the thing
```


## ⚠️ Warning Labels
- Free tier = 5000 requests/month (don't get greedy)
- Might summarize "War and Peace" as "Russia lol" 🇷🇺
- No refunds if AI calls your doc "trash" 🗑️

## 🎉 Special Thanks
- Azure for the free(ish) toys
- My cat for moral support 🐈
- Coffee ☕ (the real MVP)


# Nowego gowno
## env file
```ini
API_KEY='api'
BASE_URL='https://openrouter.ai/api/v1'
MODEL='mistralai/mistral-small-3.1-24b-instruct:free'
```