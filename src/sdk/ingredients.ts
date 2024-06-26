/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { SDK_METADATA, SDKOptions, serverURLFromOptions } from "../lib/config";
import * as enc$ from "../lib/encodings";
import { HTTPClient } from "../lib/http";
import { ClientSDK, RequestOptions } from "../lib/sdks";
import * as models from "../models";

export class Ingredients extends ClientSDK {
    private readonly options$: SDKOptions;

    constructor(options: SDKOptions = {}) {
        super({
            client: options.httpClient || new HTTPClient(),
            baseURL: serverURLFromOptions(options),
        });

        this.options$ = options;
        void this.options$;
    }
    /**
     * Get a list of ingredients.
     *
     * @remarks
     * Get a list of ingredients, if authenticated this will include stock levels and product codes otherwise it will only include public information.
     */
    async listIngredients(
        ingredients?: Array<string> | undefined,
        options?: RequestOptions
    ): Promise<models.ListIngredientsResponse> {
        const input: models.ListIngredientsRequest = {
            ingredients: ingredients,
        };
        const headers = new Headers();
        headers.set("user-agent", SDK_METADATA.userAgent);
        headers.set("Accept", "application/json");

        const payload = models.ListIngredientsRequest$.outboundSchema.parse(input);
        const body = null;

        const path = this.templateURLComponent("/ingredients")();

        const query = [
            enc$.encodeForm("ingredients", payload.ingredients, {
                explode: false,
                charEncoding: "percent",
            }),
        ]
            .filter(Boolean)
            .join("&");

        const security =
            typeof this.options$.security === "function"
                ? await this.options$.security()
                : this.options$.security;
        const securitySettings = this.resolveGlobalSecurity(security);

        const response = await this.fetch$(
            { security: securitySettings, method: "get", path, headers, query, body },
            options
        );

        const responseFields = {
            ContentType: response.headers.get("content-type") ?? "application/octet-stream",
            StatusCode: response.status,
            RawResponse: response,
        };

        if (this.matchResponse(response, 200, "application/json")) {
            const responseBody = await response.json();
            const result = models.ListIngredientsResponse$.inboundSchema.parse({
                ...responseFields,
                classes: responseBody,
            });
            return result;
        } else if (this.matchResponse(response, "5XX", "application/json")) {
            const responseBody = await response.json();
            const result = models.APIError$.inboundSchema.parse({
                ...responseFields,
                ...responseBody,
            });
            throw new models.APIError(result);
        } else if (this.matchResponse(response, "default", "application/json")) {
            const responseBody = await response.json();
            const result = models.ListIngredientsResponse$.inboundSchema.parse({
                ...responseFields,
                Error: responseBody,
            });
            return result;
        } else {
            const responseBody = await response.text();
            throw new models.SDKError("Unexpected API response", response, responseBody);
        }
    }
}
