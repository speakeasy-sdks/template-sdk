/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { IngredientType, IngredientType$ } from "./ingredienttype";
import { z } from "zod";

export type IngredientInput = {
    /**
     * The name of the ingredient.
     */
    name: string;
    /**
     * The product code of the ingredient, only available when authenticated.
     */
    productCode?: string | undefined;
    /**
     * The type of ingredient.
     */
    type: IngredientType;
};

/** @internal */
export namespace IngredientInput$ {
    export type Inbound = {
        name: string;
        productCode?: string | undefined;
        type: IngredientType;
    };

    export const inboundSchema: z.ZodType<IngredientInput, z.ZodTypeDef, Inbound> = z
        .object({
            name: z.string(),
            productCode: z.string().optional(),
            type: IngredientType$,
        })
        .transform((v) => {
            return {
                name: v.name,
                ...(v.productCode === undefined ? null : { productCode: v.productCode }),
                type: v.type,
            };
        });

    export type Outbound = {
        name: string;
        productCode?: string | undefined;
        type: IngredientType;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, IngredientInput> = z
        .object({
            name: z.string(),
            productCode: z.string().optional(),
            type: IngredientType$,
        })
        .transform((v) => {
            return {
                name: v.name,
                ...(v.productCode === undefined ? null : { productCode: v.productCode }),
                type: v.type,
            };
        });
}
