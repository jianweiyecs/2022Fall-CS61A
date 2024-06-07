const network = new Network("https://disc.cs61a.org")

class Storable {
    constructor($node) {
        this.$node = $node;
        this.$status = $node.nextAll(".storable-status").first();
        this.initialized = false;
        this.connected = false;
        this.networkReady = true;
    }

    displayNetworkReady() {
        this.$status.html("");
        $(".storable-login-status").html(
            `<p>
            You are currently logged in, so your work will be saved for you to re-visit later.
            <p>
            <button id="disc-clear-btn" class="btn btn-outline">Clear your saved answers on all worksheets</button>`);
        $(".storable-login-status").removeClass("alert-danger").addClass("alert-success");
        $("#disc-clear-btn").click(() => {
            if (window.confirm("Do you really want to clear your answers on all 61A worksheets?")) {
                this.clearStoredData();
            }
        });
    }

    async clearStoredData() {
        const success = await network.genClear();
        if (success) {
            window.location.reload();
        } else {
            this.displayNetworkNotReady();
        }
    };

    displayNetworkNotReady() {
        this.$status.html(`<a href="${network.getLoginURL()}" target="_blank">Log in to save your work!</a>`);
        $(".storable-login-status").html(
            `To be able to save your progress on this online worksheet,
            please <a href="${network.getLoginURL()}" target="_blank">log in</a>.`);
        $(".storable-login-status").removeClass("alert-success").addClass("alert-danger");
    }

    async init() {
        this.$status.html(`Loading...`);

        this.networkReady = await network.genReady();

        const genSave = async (name, value) => {
            this.$status.html("Saving...");
            const success = await network.genSave(name, value);
            if (success) {
                if (this.$status.length) {
                    this.$status.html("Saved at " + new Date() + ".");
                }
            } else {
                this.networkReady = false;
                this.displayNetworkNotReady();
                window.open(network.getLoginURL(), "_blank");
            }
        }

        if (this.networkReady) {
            this.displayNetworkReady();
            if (!this.connected) {
                await this.genConnect(network, $.debounce(1000, genSave));
                this.connected = true;
            }
        } else {
            this.displayNetworkNotReady();
        }

        if (!this.initialized) {
            window.addEventListener("focus", async () => {
                if (!this.networkReady) {
                    this.init();
                }
            });
        }
        this.initialized = true;
    }
}

class TextInputStorable extends Storable {
    constructor($node) {
        super($node);
        this.name = $node.attr("id");
    }

    lock() {
        this.$node.prop("readonly", true);
    }

    async genConnect(network, genSave) {
        const storedVal = await network.genSavedValue(this.name);
        this.$node.val(storedVal);
        this.$node.prop("readonly", false);
        const handler = () => genSave(this.name, this.$node.val())
        this.$node.on("change", handler);
        this.$node.on("keypress", handler);
        this.$node.on("blur", handler);
    }
}

$(".storable").each(function() {
    new TextInputStorable($(this)).init();
});
