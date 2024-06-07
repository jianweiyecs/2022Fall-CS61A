class EnvDiagramStorable extends Storable {
    constructor($node) {
        super($node);
        const $status = this.$status;
        $node.find(".env-text-storable").each(function () {
            new EnvDiagramTextInputStorable($(this), $status).init();
        });
        this.name = $node.attr("id");
        this.plumber = jsPlumb.getInstance();
        this.startConnector = null;
    }

    // plumbing utilities
    makeConnection(startConnector, endConnector) {
        this.plumber.setContainer(this.$node);
        this.plumber.connect({
            source: startConnector, target: endConnector,
            anchor: "Center", endpoint: "Blank",
            paintStyle: { strokeWidth:2 }
        });
    }

    removeConnectionsFrom(startConnector, genSave) {
        var connections = this.plumber.getConnections({source: startConnector});
        connections.forEach(this.plumber.deleteConnection);
        genSave("env-diagram-connection:" + startConnector.id, null);
    };

    resetStartConnector() {
        $(this.startConnector).removeClass("env-diagram-selected")
        this.startConnector = null;
    }

    getStorageKey(connector) {
        return "env-diagram-connection:" + connector.id;
    }

    // storable logic
    async genConnect(network, genSave) {
        const self = this;
        jsPlumb.ready(() => {
            this.$node.find(".env-diagram-frame .env-diagram-connector").each(async function() {
                const endId = await network.genSavedValue(self.getStorageKey(this));
                if (endId) {
                    self.makeConnection(this, document.getElementById(endId))
                }
            });
        });

        this.$node.find(".env-diagram-frame .env-diagram-connector").off("click.frame").on("click.frame", function() {
            if (self.startConnector === this) {
                self.resetStartConnector();
            } else {
                $(self.startConnector).removeClass("env-diagram-selected");
                $(this).addClass("env-diagram-selected");
                self.startConnector = this;
            }
        });
        this.$node.find(".env-diagram-objects .env-diagram-connector").off("click.object").on("click.object", function() {
            if (!self.startConnector) return;
            self.removeConnectionsFrom(self.startConnector, genSave);

            const endConnector = this;
            self.makeConnection(self.startConnector, endConnector);
            genSave(self.getStorageKey(self.startConnector), endConnector.id)
            self.resetStartConnector();
        });
        this.$node.find(".env-diagram-objects .env-diagram-trash").off("click.trash").on("click.trash", function() {
            if (!self.startConnector) return;
            self.removeConnectionsFrom(self.startConnector, genSave);
            self.resetStartConnector();
        });
    }
}

class EnvDiagramTextInputStorable extends TextInputStorable {
    constructor($node, $status) {
        super($node);
        this.$status = $status;
    }
}

$(".env-diagram").each(function() {
      new EnvDiagramStorable($(this)).init();
});
