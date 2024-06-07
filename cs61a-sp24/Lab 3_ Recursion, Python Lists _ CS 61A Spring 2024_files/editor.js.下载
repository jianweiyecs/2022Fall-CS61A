class MonacoStorable extends Storable {
    constructor($node) {
        super($node);
        this.name = $node.attr("id");
        this.editor = $node.data("editor");
        this.lockDisposable = null;
    }

    lock() {
        this.editor.updateOptions({ readOnly: true });
        const messageContribution = this.editor.getContribution('editor.contrib.messageController');
        // due to https://github.com/microsoft/monaco-editor/issues/1873, editor.onDidAttemptReadOnlyEdit()
        // doesn't work, so we implement it manually
        this.lockDisposable = this.editor.onKeyDown((e) => {
            if (!e.ctrlKey && !e.altKey && !e.metaKey) {
                messageContribution.showMessage('You must log in to edit.', this.editor.getPosition());
            }
        });
    }

    async genConnect(network, genSave) {
        const storedVal = await network.genSavedValue(this.name);
        if (storedVal != null) {
            this.editor.getModel().setValue(storedVal, 1);
        }
        this.editor.updateOptions({ readOnly: false });
        if (this.lockDisposable) {
            this.lockDisposable.dispose();
            this.lockDisposable = null;
        }
        this.editor.onDidChangeModelContent(() => genSave(this.name, this.editor.getModel().getValue()));
    }
}

function activateEditor(template, language, id) {
    const domain = "https://code.cs61a.org"

    const unescape = (string) => {
        const span = document.createElement("span");
        span.innerHTML = string;
        return span.innerText;
    };

    $(document.getElementById(`modal-link-${id}`)).click(() => {
        $(document.getElementById(`modal-${id}`)).modal();
    });

    require(["vs/editor/editor.main"], function () {
        const editor = monaco.editor.create(document.getElementById(id), {
            value: unescape(template),
            language,
            scrollBeyondLastLine: false,
            automaticLayout: true,
            minimap: {
                enabled: false
            },
            theme: "vs-dark",
        });
        $(document.getElementById(id)).data("editor", editor);
        new MonacoStorable($(document.getElementById(id))).init();
        $(document.getElementById(`modal-${id}`)).on('shown.bs.modal', function () {
            const target = domain + "/embed?" + [
                "fileName=" + encodeURIComponent("Untitled"),
                "data=" + encodeURIComponent(editor.getModel().getValue().slice(0, 1024)),
                "srcOrigin=" + encodeURIComponent(window.origin),
            ].join("&");
            $(this).find('iframe').attr('src', target);
        });
        const iframeWindow = $(document.getElementById(`code-iframe-${id}`)).get(0).contentWindow;
        window.addEventListener("message", message => {
            if (message.source !== iframeWindow) {
                return;
            }
            if (message.data.requestData) {
                iframeWindow.postMessage(editor.getModel().getValue(), domain);
            } else {
                editor.getModel().setValue(message.data.data);
            }
        });
    });
}
