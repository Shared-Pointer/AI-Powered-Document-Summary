.PHONY: build run run-dev

IMAGE_NAME = ai-document-summarizer
CONTAINER_NAME = summarizer
PORT = 8501

build:
	@docker build -t $(IMAGE_NAME) .

run:
	@docker run -it --rm -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

clean:
	@docker rmi $(IMAGE_NAME) || true

stop:
	@docker stop $(CONTAINER_NAME) || true
