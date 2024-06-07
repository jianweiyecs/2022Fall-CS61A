class Network {
    constructor(provider = "https://disc.cs61a.org") {
        this.provider = provider;
        this.loadedData = null;
        this.savedDataPromise = null;
    }

    getLoginURL = () => {
        return `${this.provider}/oauth/login`
    }

    genAllSavedData = async () => {
        if (this.loadedData) {
            return this.loadedData;
        }
        try {
            if (this.savedDataPromise == null) {
                this.savedDataPromise = this.genPost("fetch");
            }
            this.loadedData = await this.savedDataPromise;
        } catch {
            return null;
        } finally {
            this.savedDataPromise = null;
        }
        return this.loadedData;
    }

    genReady = async () => {
        // clear cache
        // do not clear in-flight promise
        this.loadedData = null;
        return (await this.genAllSavedData()) != null;
    }

    genSavedValue = async (name) => {
        const loadedData = await this.genAllSavedData();
        return loadedData?.[name];
    }

    genSave = async (name, value) => {
        try {
            await this.genPost("save", {name, value});
        } catch {
            return false;
        }
        return true;
    }

    genClear = async () => {
        try {
            await this.genPost("clear");
        } catch {
            return false;
        }
        return true;
    }

    genPost = async (endpoint, payload = {}) => {
        const resp = await fetch(`${this.provider}/${endpoint}`, {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });
        return resp.json();
    }
}
