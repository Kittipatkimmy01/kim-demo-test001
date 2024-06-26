odoo.define("withholding_tax_report_backend", function (require) {
    "use strict";

    var AbstractAction = require("web.AbstractAction");
    var core = require("web.core");
    var ReportWidget = require("withholding_tax_report_widget");

    var report_backend = AbstractAction.extend({
        hasControlPanel: true,
        // Stores all the parameters of the action.
        events: {
            "click .o_withholding_tax_report_print": "print",
            "click .o_withholding_tax_report_export": "export",
        },
        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.actionManager = parent;
            this.given_context = {};
            this.odoo_context = action.context;
            this.controller_url = action.context.url;
            if (action.context.context) {
                this.given_context = action.context.context;
            }
            this.given_context.active_id =
                action.context.active_id || action.params.active_id;
            this.given_context.model = action.context.active_model || false;
            this.given_context.ttype = action.context.ttype || false;
        },
        willStart: function () {
            return Promise.all([this._super.apply(this, arguments), this.get_html()]);
        },
        set_html: function () {
            var self = this;
            var def = Promise.resolve();
            if (!this.report_widget) {
                this.report_widget = new ReportWidget(this, this.given_context);
                def = this.report_widget.appendTo(this.$(".o_content"));
            }
            def.then(function () {
                self.report_widget.$el.html(self.html);
            });
        },
        start: function () {
            this.set_html();
            return this._super();
        },
        // Fetches the html and is previous report.context if any,
        // else create it
        get_html: function () {
            var self = this;
            var defs = [];
            return this._rpc({
                model: this.given_context.model,
                method: "get_html",
                args: [self.given_context],
                context: self.odoo_context,
            }).then(function (result) {
                self.html = result.html;
                defs.push(self.update_cp());
                return Promise.all(defs);
            });
        },
        // Updates the control panel and render the elements that have yet
        // to be rendered
        update_cp: function () {
            if (this.$buttons) {
                var status = {
                    breadcrumbs: this.actionManager.get_breadcrumbs(),
                    cp_content: {$buttons: this.$buttons},
                };
                return this.updateControlPanel(status);
            }
        },
        do_show: function () {
            this._super();
            this.update_cp();
        },
        print: function () {
            window.print();
        },
        export: function () {
            var self = this;
            this._rpc({
                model: this.given_context.model,
                method: "print_report",
                args: [this.given_context.active_id, "xlsx"],
                context: self.odoo_context,
            }).then(function (result) {
                self.do_action(result);
            });
        },
        canBeRemoved: function () {
            return Promise.resolve();
        },
    });

    core.action_registry.add("withholding_tax_report_backend", report_backend);
    return report_backend;
});
