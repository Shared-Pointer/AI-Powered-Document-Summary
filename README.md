# 🦄 KakaSummary - Silly AI Doc Crusher

*"Because reading is for nerds, summarizing is for cool kids"* - Sun Tzu probably

## 🎪 What's this circus about?
A magical AI that turns your boring long documents into... slightly less boring short documents! Powered by ~~Azure's~~ OpenRouter brain juice and student tears.

---

## 🧞‍♂️ OpenRouter Vibes (Free Magic Edition)

### Numero uno - OpenRouter Shenanigans
1. Create an account at [OpenRouter](https://openrouter.ai/) — yes, it’s real, and no, it's not a Wi-Fi company.
2. Summon your **API key** from the shadows (or your [dashboard](https://openrouter.ai/account/keys)).
3. Choose a model — for this silly quest, I picked [**Mistral Small 3.1 24B (free)**](https://openrouter.ai/mistralai/mistral-small-3.1-24b-instruct:free) because it sounds fancy.
4. Pick the **Free plan** — because we’re broke but curious.
5. Browse other free models if you feel spicy 🌶️ — this one’s just a humble suggestion.

### Numero dos - The Sacred `.env` Scrolls 🧻

Once you’ve tricked the system into trusting you, create a `.env` file inside `config/` (don’t ask, just do it).

```ini
API_KEY='your-api-key-here'  # secret sauce
BASE_URL='https://openrouter.ai/api/v1'  # the mothership
MODEL='mistralai/mistral-small-3.1-24b-instruct:free'  # free = best flavor
```


## 🚀 Launch Protocol (for dummies)
### Option A: Docker Magic 🐳
```
make build  # Wait for the robot to think
make run    # Unleash the beast
```
Then point browser to http://localhost:8501 and pray 🙏

### Option B: Manual Mode 🤓 (nerd) idk if it works
```
pip install -r requirements.txt  # Download internet
streamlit run app/main.py       # Do the thing
```


## ⚠️ Warning Labels
- Free tier = don't get greedy
- Might summarize "War and Peace" as "Russia lol" 🇷🇺
- No refunds if AI calls your doc "trash" 🗑️

## 🎉 Special Thanks
~~- Azure for the free(ish) toys~~
- OpenRouter for the free(ish) toys
- My cat for moral support 🐈
- White Monster Energy Drink (the real MVP)
